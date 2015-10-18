import sys
import json

scores = {}
tweets = []
tweetScores = {}


def getLocation(tweet):
    location = tweet['user']['location']
    if location != None:
        split = location.split(",")
        if len(split) > 1:
            state = split[1].strip()
            if len(state) == 2:
                # print state
                return state


def findHappiest():
    happiestScore = 0
    happiestState = ""
    for key in tweetScores.keys():
        if happiestState == "":
            happiestState = key
        thisScore = tweetScores[key]
        if(thisScore > happiestScore):
            happiestScore = thisScore
            happiestState = key
    print happiestState


def hw():
    # print 'Hello, world!'
    for tweet in tweets:
        if 'text' in tweet:
            # if tweet['lang'] == "en":
            text = tweet['text']
            score = getScore(text)
            location = getLocation(tweet)
            if location != None:
                incrementFrequency(location, score)
    # print tweetScores
    findHappiest()

def incrementFrequency(word, score):
    if(tweetScores.has_key(word)):
        frequency = tweetScores[word]
        tweetScores[word] = frequency + score
    else:
        tweetScores[word] = score


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
    # print text
    words = text.split(" ")
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

if __name__ == '__main__':
    main()