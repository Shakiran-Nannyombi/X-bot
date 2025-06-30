from flask import Flask, render_template, jsonify, request
from bot.content_generator import ContentGenerator
from config.settings import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize content generator
content_gen = ContentGenerator()

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    content_type = data.get('type', 'educational')
    topic = data.get('topic')
    
    try:
        content = content_gen.generate(content_type, topic)
        return jsonify({'content': content, 'length': len(content)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/save-notification-settings', methods=['POST'])
def save_notification_settings():
    # In a real app, you'd save this to a database
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
