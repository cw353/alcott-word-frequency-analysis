# Claire W.
# Revised version: 11 Dec. 2020
# Original version: 3-5 Dec. 2020

import re
from operator import itemgetter
from pathlib import Path
from ListOfTexts import textList
from time import time
from sys import exit

regex = re.compile(r'[^\-\'\w\s]')

words = {}

def analyzeFrequency(line):
    for k in line:
        k = k.strip('-\'’')
        if k in words:
            words[k] += 1
        else:
            words[k] = 1


def readLines(pathname):
    with open(pathname) as file:
        for line in file:
            line = file.readline()
            analyzeFrequency(regex.sub(' ',line.lower().replace(
                '’','\'')).replace('--',' ').replace('_',' ').split())


def main():
    directory = './corpus/'
    startTime = time()
    for i in textList:
        readLines(directory+i)
        
    sortByValue = itemgetter(1)
    frequencyList = list(reversed(sorted(words.items(),key=sortByValue)))
    
    with open('frequency_analysis.txt','w') as newFile:
        for i in frequencyList:
            newFile.write(i[0] + ": " + str(i[1]) + '\n')
    endTime = time()
    print('Execution time: ' + str(endTime-startTime))
    print('Total number of unique words: ' + str(len(frequencyList)))
    exit(0)

main()
