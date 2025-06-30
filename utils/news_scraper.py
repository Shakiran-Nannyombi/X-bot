"""
Tech news and trending topics scraper utility.
"""
import requests
from bs4 import BeautifulSoup

def fetch_github_trending(language=None):
    """Fetch trending repositories from GitHub Trending."""
    url = f'https://github.com/trending'
    if language:
        url += f'/{language}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    repos = []
    for repo in soup.find_all('article', class_='Box-row'):
        title = repo.h2.text.strip().replace('\n', '').replace(' ', '')
        link = 'https://github.com' + repo.h2.a['href']
        repos.append({'title': title, 'url': link})
    return repos

def fetch_hackernews_top(limit=10):
    """Fetch top stories from Hacker News."""
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stories = []
    for row in soup.find_all('tr', class_='athing')[:limit]:
        title = row.find('a', class_='storylink').text
        link = row.find('a', class_='storylink')['href']
        stories.append({'title': title, 'url': link})
    return stories

def fetch_devto_trending(limit=10):
    """Fetch trending articles from dev.to."""
    url = 'https://dev.to/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    for article in soup.find_all('h2', class_='crayons-story__title')[:limit]:
        a = article.find('a')
        title = a.text.strip()
        link = 'https://dev.to' + a['href']
        articles.append({'title': title, 'url': link})
    return articles 