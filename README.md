# X-bot

A modular Flask-based bot application with AI-powered replies, meme generation, and scheduling capabilities.

## Project Structure

```
├── app.py                # Main Flask app
├── bot/                  # Bot-related modules
│   ├── __init__.py       # Initialize bot package
│   ├── bot.py            # Main bot logic
│   ├── reply_generator.py# Functions for AI-based replies
│   ├── meme_generator.py # Meme creation logic
│   ├── scheduler.py      # Handles scheduling tasks
├── config/
│   ├── secrets.py        # API keys and secrets
│   ├── settings.py       # Configuration options
├── templates/
│   ├── base.html         # Base template
│   ├── dashboard.html    # Dashboard UI
├── static/               # Static assets (CSS, JS)
│   ├── css/
│   │   ├── styles.css    # Custom styles
├── requirements.txt      # Python dependencies
├── .gitignore            # Files to ignore in Git
├── LICENSE               # License file
├── README.md             # Project documentation
```

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   python app.py
   ```

## Features
- AI-based reply generation
- Meme creation
- Task scheduling
- Web dashboard
