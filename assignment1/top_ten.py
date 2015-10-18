import sys
import json
import operator

termFrequency = {}
terms = []
hashTagsFrequency = {}


def read_tweets(tweet_file):
    tweets = []
    for line in tweet_file.readlines():
        s  = json.loads(line)
        tweets.append(s)
    return tweets

def process(tweets):
    for tweet in tweets:
        processHashTags(tweet)

def processHashTags(tweet):
    if 'entities' in tweet:
        hashTags =  tweet["entities"]["hashtags"]
        for hashTag in hashTags:
            text = hashTag["text"].encode('utf-8').lower()
            incrementFrequency(text)


def incrementFrequency(word):
    if(hashTagsFrequency.has_key(word)):
        frequency = hashTagsFrequency[word]
        hashTagsFrequency[word] = ++frequency
    else:
        hashTagsFrequency[word] = 1


def printResult():
    sorted_x = sorted(hashTagsFrequency.items(), key=operator.itemgetter(1))
    for i in range(0,10):
        item = sorted_x[i]
        print item[0] + " " + repr(item[1])
    # print sorted_x



def main():
    tweet_file = open(sys.argv[1])
    tweets = read_tweets(tweet_file)
    process(tweets)
    printResult()


if __name__ == '__main__':
    main()