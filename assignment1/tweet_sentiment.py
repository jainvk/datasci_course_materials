import sys
import json

scores = {}
tweets = []
tweetScores = []

def hw():
    # print 'Hello, world!'
    for tweet in tweets:
        if 'text' in tweet:
            # if tweet['lang'] == "en":
            tweetScores.append(getScore(tweet['text']))
        # else:
        #     tweetScores.append(0)
    for score in tweetScores:
        print score


def lines(fp):
    print str(len(fp.readlines()))

def readAffin(file):
    # print "reading file" + file.name
    affinnfile = open(file.name)
    for line in affinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)

def readTweets(file):
    # print "reading file" + file.name
    tweetLines = open(file.name)
    for tweetLine in tweetLines:
        tweets.append(json.loads(tweetLine))


def getScore(text):
    encoded_string = text.encode('utf-8')
    # print text
    words = encoded_string.split(" ")
    score = 0
    # print words
    for word in words:
        score += scores.get(word,0)
    return score


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    readAffin(sent_file)
    # print scores
    readTweets(tweet_file)
    hw()
    # print tweetScores
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
