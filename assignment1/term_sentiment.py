import sys
import json

scores = {}
tweets = []
tweet_scores = {}

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def create_score(fp):
    for line in fp.readlines():
        term, score = line.split("\t")
        scores[term] = int(score)


def read_tweets(tweet_file):
    for line in tweet_file.readlines():
        s  = json.loads(line)
        text = ""
        if "text" in s:
            text = s["text"]
        elif "u'text'" in s:
            text = s["u'text'"]
        tweets.append(text.encode("utf-8"))


def process():
    for tweet in tweets:
        score = 0
        for word in tweet.split():
            if word in scores:
                score = score + scores[word]
        tweet_scores[tweet] = score

def process1(tweet):
    score = 0
    for word in tweet.split():
        if word in scores:
            score = score + scores[word]
    tweet_scores[tweet.tolower()] = score


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    create_score(sent_file)
    read_tweets(tweet_file)
    process()
    for tweet_score in tweet_scores:
        for word in tweet_score.split():
            print word + " " + repr(tweet_scores[tweet_score])


if __name__ == '__main__':
    main()