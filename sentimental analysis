# list of punctuation chars
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# function that to remove punctuation            
def strip_punctuation(s):
    for cha in s:
        if cha in punctuation_chars:
            s = s.replace(cha,'')         
    return s

#function to count positive words in twitter
def get_pos(s):
    words = strip_punctuation(s).split()
    n = 0
    for word in words:
        if word in positive_words:
            n += 1
    return n

# function to count negative in twitter
def get_neg(s):
    words = strip_punctuation(s).split()
    n = 0
    for word in words:
        if word in negative_words:
            n += 1
    return n

# file that needs to be analysed
fileref = open('project_twitter_data.csv')

# file that stores the result
results = open('resulting_data.csv', 'w')
results.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')

# read every line but skip the first line
for line in fileref.readlines()[1:]:
    twitter = line.split(',')
    s, Num_Retweet , Num_Reply = twitter[0], int(twitter[1]), int(twitter[2])
    Pos = get_pos(s)
    Neg = get_neg(s)
    Net = Pos - Neg
    results.write('{}, {}, {}, {}, {}\n'.format(Num_Retweet, Num_Reply, Pos, Neg, Net))
fileref.close()
results.close()
