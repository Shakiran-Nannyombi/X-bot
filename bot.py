import argparse
from utils.meme_generator import generate_meme
from utils.reply_generator import generate_reply
from utils.sentiment import analyze_sentiment
from utils.scheduler import schedule_post
from utils.llm import generate_with_llm, LLMProvider, LLMModel

# Example main bot orchestration

def main():
    parser = argparse.ArgumentParser(description="X-Bot: Content and Meme Generator")
    parser.add_argument('--meme', action='store_true', help='Generate a meme')
    parser.add_argument('--reply', type=str, help='Generate a reply to given context')
    parser.add_argument('--sentiment', type=str, help='Analyze sentiment of given text')
    parser.add_argument('--schedule', type=str, help='Schedule a post at a given time (format: "YYYY-MM-DD HH:MM")')
    parser.add_argument('--auto-content', action='store_true', help='Auto-generate content and memes for trends and user topics')
    args = parser.parse_args()

    if args.meme:
        # Example usage: generate a meme from a template and caption
        template_path = 'templates/meme_template.jpg'
        caption = input('Enter meme caption: ')
        output_path = 'generated_meme.jpg'
        generate_meme(template_path, caption, output_path)
        print(f"Meme generated and saved to {output_path}")

    if args.reply:
        context = args.reply
        reply = generate_reply(context)
        print(f"Generated reply: {reply}")

    if args.sentiment:
        text = args.sentiment
        polarity, subjectivity = analyze_sentiment(text)
        print(f"Polarity: {polarity:.3f}, Subjectivity: {subjectivity:.3f}")

    if args.schedule:
        time_str = args.schedule
        content = input('Enter content to schedule: ')
        schedule_post(time_str, content)
        print(f"Scheduled post at {time_str}")

    if args.auto_content:
        import os
        from utils.news_scraper import fetch_github_trending, fetch_hackernews_top, fetch_devto_trending
        from utils.llm import generate_with_llm
        import datetime

        # User topics
        user_topics = [
            "education", "jokes", "new tech", "tutorial", "open source documents", "datascience",
            "book recommendation", "roadmaps", "career guide", "tech beginner", "content to attract people to tech",
            "unrelated but funny captivating content"
        ]

        # Fetch trends
        print("Fetching trending topics...")
        trends = []
        try:
            trends += [repo['title'] for repo in fetch_github_trending()[:3]]
        except Exception as e:
            print(f"Error fetching GitHub trends: {e}")
        try:
            trends += [story['title'] for story in fetch_hackernews_top(3)]
        except Exception as e:
            print(f"Error fetching Hacker News: {e}")
        try:
            trends += [article['title'] for article in fetch_devto_trending(3)]
        except Exception as e:
            print(f"Error fetching Dev.to: {e}")

        topics = user_topics + trends
        print(f"Generating content for {len(topics)} topics...")

        output_dir = "auto_content_output"
        os.makedirs(output_dir, exist_ok=True)
        summary = []
        for topic in topics:
            # Generate post
            prompt = f"Write a captivating social media post about: {topic}"
            post = generate_with_llm(
                prompt,
                model=LLMModel.GPT_4O,  # Change to GEMINI_FLASH or OLLAMA_LLAMA3 if desired
                provider=LLMProvider.OPENAI  # Change to GEMINI or OLLAMA if desired
            )
            # Generate meme
            meme_caption = f"{topic} - {post[:60]}..."
            meme_path = os.path.join(output_dir, f"meme_{topic[:15].replace(' ','_')}.jpg")
            generate_meme("templates/meme_template.jpg", meme_caption, meme_path)
            # Save post
            post_path = os.path.join(output_dir, f"post_{topic[:15].replace(' ','_')}.txt")
            with open(post_path, 'w', encoding='utf-8') as f:
                f.write(post)
            summary.append((topic, post_path, meme_path))
            print(f"Generated for topic: {topic}")
        print(f"\nAuto content generation complete. Results saved in '{output_dir}'.")
        print("Summary:")
        for topic, post_path, meme_path in summary:
            print(f"- {topic}: post -> {post_path}, meme -> {meme_path}")

if __name__ == "__main__":
    main() 