from nltk.tokenize import word_tokenize,sent_tokenize,RegexpTokenizer
from nltk.corpus import stopwords,wordnet
from nltk import pos_tag
from string import punctuation
import pandas,csv,ast

def tokenize_words(mystring):
    tokenizer = RegexpTokenizer("[\w']+")
    return tokenizer.tokenize(mystring)

def tokenize_sentences(mystring):
    return sent_tokenize(mystring)

def pos_tagging(mydict):
    my_dict = {}
    for key,value in mydict.iteritems():
        my_dict.setdefault(key,[])
        mylist= tokenize_words(value)
        mysecondlist = tokenize_words(key)
        my_dict[key].append(pos_tag(mysecondlist))
        my_dict[key].append(pos_tag(mylist))
    return my_dict
    
english_stops = set(stopwords.words('english'))

colnames = ['Sender','Receiver','Subject','Body']
data = pandas.read_csv('emaildata.csv',names=colnames)

subject = list(data.Subject)
body = list(data.Body)

mydict = dict(zip(subject,body))

pos_dict = pos_tagging(mydict)

pos_sent = open("positive.txt").read()
positive_words = pos_sent.split("\n")
positive_count = []

neg_sent = open("negative.txt").read()
negative_words = neg_sent.split("\n")
negative_count = []

#print pos_dict


new_dict = {}
mylist = []
tempthree = []        
reqlist = ['VBN','JJ']
for key,value in pos_dict.iteritems():
    temptwo = []
    for klst in value:
        temp = []
        for lst in klst:
            if lst[1] in reqlist:
                print lst[0]
                temp.append(lst[0])
        temptwo.append(temp)
    mylist.append(key)
    tempthree.append(temptwo)
new_dict = dict(zip(mylist,tempthree))

print new_dict


for key,value in new_dict.iteritems():
    positive_counter = 0
    negative_counter = 0

    for klst in value:
        for lst in klst:
            for go in lst:
                go = go.lower()    
    #value_processed = value.lower()


    for klst in value:
        for lst in klst:
            for go in lst:
                for p in list(punctuation):
                    go = go.replace(p,'')

    #words = value_processed.split(' ')
    #word_count = len(words)

    for klst in value:
        for lst in klst:
            for word in lst:
                if word in positive_words:
                    positive_counter += 1
                elif word in negative_words:
                    negative_counter += 1
        #print positive_counter + negative_counter

      
output = zip(value,positive_count,negative_count)

writer = csv.writer(open('email_sentiment.csv','wb'))
writer.writerows(output)






