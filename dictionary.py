import urllib.request
import re
import csv

writer=csv.writer(open('output.csv','w'))

while True:

    word=input("请打出你想差的英语单词(并用空格隔开)")#user inputs words he wants to look up
    word2=word.split(" ")# creates list of words
    word3=sorted(word2, key=len)#sorts the words in the list from shortest to longest
    print(word3)

    if word == 'q':
        print('thanks for using my amazing dictionary app')
        break

    for x in word3:
        url="http://www.merriam-webster.com/dictionary/" #link
        word=x
        url=url+word #concatenate url and word to form the final url
        text=urllib.request.urlopen(url).read().decode('utf-8') #open the url, read it and change the encoding to utf-8. Needed to use regex on it
        a=re.findall('<span><span class="intro-colon">:</span>(.+?)</span>', text) #regex finds all occurences of the specific

        if a == []:
            print('word not found')
            break

        print(a)
        a.insert(0, word) # add word as first column
        writer.writerow(a)

        #file=open("words.txt","a")
        #file.write(','.join(a))
        #file.close
        #file=open("words.txt","r")
        #file.close
