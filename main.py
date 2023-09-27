import sent_analyzer
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            prog='News Sentiment Analyzer',
            description='Analyzes news websites for textual sentiment',
            )
    parser.add_argument('urls')
    parser.add_argument('-f', '--f', action='store_true', dest='file')

    args = parser.parse_args()
    urls = args.urls
    file = args.file
    if file is True:
        f = open(urls, "r")
        for line in f:
            sent_analyzer.get_sentiment(line)
    else:
        sent_analyzer.get_sentiment(urls)
