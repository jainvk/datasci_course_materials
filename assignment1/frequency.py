import sys
import json

termFrequency = {}
terms = []

def read_tweets(tweet_file):
    tweets = []
    for line in tweet_file.readlines():
        s  = json.loads(line)
        text = ""
        if "text" in s:
            text = s["text"]
        elif "u'text'" in s:
            text = s["u'text'"]
        tweets.append(text.encode("utf-8"))
    return tweets


def incrementFrequency(word):
    if(termFrequency.has_key(word)):
        frequency = termFrequency[word]
        termFrequency[word] = ++frequency
    else:
        termFrequency[word] = 1


def process(tweets):
    for tweet in tweets:
        for word in tweet.split():
            if word not in terms:
                terms.append(word)
                incrementFrequency(word)



def main():
    tweet_file = open(sys.argv[1])
    tweets = read_tweets(tweet_file)
    process(tweets)
    for term in terms:
        print term + " " + repr(termFrequency[term])


if __name__ == '__main__':
    main()