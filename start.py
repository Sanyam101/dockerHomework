import os
import itertools

def files(dir):
    fileList = []
    txtFile=0
    for file in os.listdir(dir):
        if file.endswith(".txt"):
            txtFile+=1
            fileList.append(file)
    print("\n\nList of Text Files:")
    print(*fileList, sep = "\n")
    print ("\n\nTotal Number of text files = ",txtFile,"\n\n")

def wordCount(dir):
    countList = []
    for file in os.listdir(dir):
        if file.endswith(".txt"):
            num_words = 0
            fname =os.path.join(dir, file)
            with open(fname, 'r') as f:
                for line in f:
                    words = line.split()
                    num_words += len(words)
            countList.append(num_words)
        print("Number of words in ",file," : ",num_words)
    print("\n\nTotal Word Count is :",sum(countList))

def commonWord(dir):
    freqList = []
    for file in os.listdir(dir):
        if file.endswith(".txt"):
            fname =os.path.join(dir, file)
            with open(fname, 'r') as f:
                for line in f:
                    words = line.split()
                    propWord=[word for word in words if len(word) >= 5]
                    freqList.append(propWord)
    #print(freqList)
    wordList = list(itertools.chain.from_iterable(freqList))
    wordList = [x.lower() for x in wordList]
    #print(wordList)
    di = dict()
    for w in wordList:
        di[w] = di.get(w,0) + 1
    #print(di)
    maxValue = 0
    for word,freq in di.items():
        if freq > maxValue:
            maxValue = freq
            commonWrd = word
    print("\n\nMost frequent occuring word is :",commonWrd,", and it occurs", maxValue,"times")



#def uncommonWord(dir):

files("./data")
wordCount("./data")
commonWord("./data")
