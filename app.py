import os
import tempfile

from flask import Flask, render_template, jsonify, request, send_file
# from bot.content_generator import ContentGenerator
from config.settings import Config
from utils.llm import generate_with_llm
from dotenv import load_dotenv
from utils.meme_generator import generate_meme
from utils.news_scraper import fetch_github_trending, fetch_hackernews_top, fetch_devto_trending
from utils.sentiment import analyze_sentiment
from utils.analytics import save_content_to_csv

load_dotenv()

app = Flask("Kiran's X-Bot")
app.config.from_object(Config)

# Initialize content generator
# content_gen = ContentGenerator()

# In-memory content store for demonstration
GENERATED_CONTENT = []

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    content_type = data.get('type', 'educational')
    topic = data.get('topic')
    
    try:
        # content = content_gen.generate(content_type, topic)
        return jsonify({'content': content, 'length': len(content)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/save-notification-settings', methods=['POST'])
def save_notification_settings():
    # In a real app, you'd save this to a database
    return jsonify({'success': True})

@app.route('/ai-generate', methods=['POST'])
def ai_generate():
    data = request.json
    prompt = data.get('prompt')
    provider = data.get('provider', 'openai')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    try:
        result = generate_with_llm(prompt, provider=provider)
        return jsonify({'content': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate-meme', methods=['POST'])
def generate_meme_route():
    if 'template' not in request.files or 'caption' not in request.form:
        return jsonify({'error': 'Template image and caption are required.'}), 400
    template = request.files['template']
    caption = request.form['caption']
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_template:
        template.save(temp_template.name)
        output_path = temp_template.name + '_meme.jpg'
        generate_meme(temp_template.name, caption, output_path)
        return send_file(output_path, mimetype='image/jpeg', as_attachment=False)

@app.route('/fetch-github-trending')
def github_trending():
    language = request.args.get('language')
    try:
        repos = fetch_github_trending(language)
        return jsonify({'results': repos})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/fetch-hackernews')
def hackernews():
    try:
        stories = fetch_hackernews_top()
        return jsonify({'results': stories})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/fetch-devto')
def devto():
    try:
        articles = fetch_devto_trending()
        return jsonify({'results': articles})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/analyze-sentiment', methods=['POST'])
def analyze_sentiment_route():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({'error': 'Text is required.'}), 400
    polarity, subjectivity = analyze_sentiment(text)
    return jsonify({'polarity': polarity, 'subjectivity': subjectivity})

@app.route('/save-content', methods=['POST'])
def save_content():
    data = request.json
    if not data or 'content' not in data:
        return jsonify({'error': 'Content is required.'}), 400
    GENERATED_CONTENT.append(data)
    return jsonify({'success': True})

@app.route('/export-content')
def export_content():
    if not GENERATED_CONTENT:
        return jsonify({'error': 'No content to export.'}), 400
    with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as temp_csv:
        save_content_to_csv(GENERATED_CONTENT, temp_csv.name)
        temp_csv.flush()
        return send_file(temp_csv.name, mimetype='text/csv', as_attachment=True, download_name='generated_content.csv')

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
