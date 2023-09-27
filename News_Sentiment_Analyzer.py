import nltk
nltk.download('vader_lexicon')
import requests
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer


def scrape_news(url):
    """Scrapes the top headlines from a news website."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    news_list = soup.find_all("item")
    return news_list


def analyze_sentiment(news_list):
    """Analyzes the sentiment of the top headlines from a news website."""
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []
    for news in news_list:
        title_sentiment = analyzer.polarity_scores(news.title.text)

    description_sentiment = analyzer.polarity_scores(news.description.text)
    sentiments.append((title_sentiment, description_sentiment))
    return sentiments


def sum_sentiment_scores(sentiments):
    """Sums the values in the 'neg', 'neu', and 'pos' columns of the sentiment scores."""
    neg_sum = 0
    neu_sum = 0
    pos_sum = 0
    for title_sentiment, description_sentiment in sentiments:
        neg_sum += title_sentiment['neg'] + description_sentiment['neg']
        neu_sum += title_sentiment['neu'] + description_sentiment['neu']
        pos_sum += title_sentiment['pos'] + description_sentiment['pos']
    return neg_sum, neu_sum, pos_sum


# userterm = input()


if __name__ == "__main__":
    url = "https://news.google.com/news/rss"
    # url = "https://news.google.com/rss/search?q=stocks&hl=en-US&gl=US&ceid=US%3Aen"
    # url = "https://news.google.com/rss/search?q=bonds&hl=en-US&gl=US&ceid=US%3Aen"
    # url = "https://news.google.com/rss/search?q=earnings&hl=en-US&gl=US&ceid=US%3Aen"
    # url = "https://news.google.com/rss/search?q=netflix&hl=en-US&gl=US&ceid=US%3Aen"
    # url = "https://www.npr.org/sections/news/"
    # url = "http://feeds.bbci.co.uk/news/rss.xml"
    # url = "https://www.ft.com/news-feed/rss.xml"
    # url = "https://www.nasdaq.com/feed/rssoutbound?category=Stocks/rss.xml"
    # url = "https://news.google.com/rss/search?q=when:24h+allinurl:bloomberg.com&hl=en-US&gl=US&ceid=US:en"
    # url = "https://news.google.com/rss/search?gl=US&hl=en-US&q=Tesla,+Inc.&ceid=US:en"
    # url = "https://news.google.com/rss/search?q=when:24h+allinurl:bloomberg.com"
    # url = "https://rss.nytimes.com/services/xml/rss/nyt/MostViewed.xml"
    news_list = scrape_news(url)
    sentiments = analyze_sentiment(news_list)
    neg_sum, neu_sum, pos_sum = sum_sentiment_scores(sentiments)
    print("Negative sentiment:", neg_sum)
    print("Neutral sentiment:", neu_sum)
    print("Positive sentiment:", pos_sum)
    print("Positive - Negative Difference: ", pos_sum-neg_sum)
