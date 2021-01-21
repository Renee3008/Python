'''This project is useful to read the file and find out the count of each word'''

#CountitDude 
import operator
import sys

#Read the File
#file=open("news.txt","r")

file=open(sys.argv[1],"r")

contents=file.read()
file.close()
#print(contents)

print(sys.argv)

#Get the Count of words
allWords={}
for word in contents.split():
    if word.lower() in allWords:
            allWords[word.lower()]+=1
    else:
            allWords[word.lower()]=1

# Descending order for count
sortedWords=sorted(allWords.items(),key=operator.itemgetter(1),reverse=True)

#print("Total Words : "+str(allWords.count()))
#print(allWords)
#file=open("news-count.txt","w")
newFile=sys.argv[1][:-4]+"-Count"+sys.argv[1][-4:]
print(newFile)
file=open(newFile,"w")

file.write("Total Words : {}\nUnique Words: {}\n\n".format(len(contents.split()),len(sortedWords)))
for wordinfo in sortedWords:
    file.write("{} - {}\n".format(wordinfo[0],wordinfo[1]))
file.close()



#Close the File