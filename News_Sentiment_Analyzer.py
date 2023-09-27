import nltk
import requests
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


def scrape_news(url: str) -> []:
    """Scrapes the top headlines from a news website."""

    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.Timeout as err:
        print("Error Recieved: ", err)
        return []

    soup = BeautifulSoup(response.content, "xml")
    news_list = soup.find_all("item")
    return news_list


def analyze_sentiment(news_list) -> [int]:
    """Analyzes the sentiment of the top headlines from a news website.
    If news_list is empty, returns sentiments of 0
    """
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []
    if len(news_list) != 0:
        for news in news_list:
            title_sentiment = analyzer.polarity_scores(news.title.text)

        description_sentiment = analyzer.polarity_scores(news.description.text)
        sentiments.append((title_sentiment, description_sentiment))
        return sentiments
    return sentiments


def sum_sentiment_scores(sentiments: [int]):
    """Sums the values in the 'neg', 'neu', and 'pos'
    columns of the sentiment scores."""
    if len(sentiments) != 0:
        neg_sum = 0
        neu_sum = 0
        pos_sum = 0
        for title_sentiment, description_sentiment in sentiments:
            neg_sum += title_sentiment['neg'] + description_sentiment['neg']
            neu_sum += title_sentiment['neu'] + description_sentiment['neu']
            pos_sum += title_sentiment['pos'] + description_sentiment['pos']
        return neg_sum, neu_sum, pos_sum
    return 0, 0, 0


def get_sentiment(urls):
    for url in urls:
        print("===== " + url + " =====")
        news_list = scrape_news(url)
        sentiments = analyze_sentiment(news_list)
        print(type(news_list))
        neg_sum, neu_sum, pos_sum = sum_sentiment_scores(sentiments)

        print("    Negative sentiment:", neg_sum)
        print("    Neutral sentiment:", neu_sum)
        print("    Positive sentiment:", pos_sum)
        print("    Positive - Negative Difference: ", pos_sum-neg_sum, "\n")


if __name__ == "__main__":
    urls = [
        "https://news.google.com/news/rss",
        "https://news.google.com/rss/search?q=stocks&hl=en-US&gl=US&ceid=US%3Aen",
        "https://news.google.com/rss/search?q=bonds&hl=en-US&gl=US&ceid=US%3Aen",
        "https://news.google.com/rss/search?q=earnings&hl=en-US&gl=US&ceid=US%3Aen",
        "https://news.google.com/rss/search?q=netflix&hl=en-US&gl=US&ceid=US%3Aen",
        "https://www.npr.org/sections/news/",
        "http://feeds.bbci.co.uk/news/rss.xml",
        "https://www.ft.com/news-feed/rss.xml",
        "https://www.nasdaq.com/feed/rssoutbound?category=Stocks/rss.xml",
        "https://news.google.com/rss/search?q=when:24h+allinurl:bloomberg.com&hl=en-US&gl=US&ceid=US:en",
        "https://news.google.com/rss/search?gl=US&hl=en-US&q=Tesla,+Inc.&ceid=US:en",
        "https://news.google.com/rss/search?q=when:24h+allinurl:bloomberg.com",
        "https://rss.nytimes.com/services/xml/rss/nyt/MostViewed.xml",
    ]
