# -*- coding: <utf-8> -*-

import sys
import os
import contextlib
import re


def processFile(file):

    # Initial dictionary declaration {(word1, value), (word2, value), ... ect.}
    wordDict = {}

    # This variable is later used to make the output look more neat.
    maxWordLength = 0

    with open(file, 'r', encoding='utf8') as f:
        for line in f:
            # These 3 lines 1st remove all punctuation except for
            #   apostrophes, strip the line of it's endline character
            #   and then lowercases all of it
            # This is done to prepare the words in each line to
            #   be processed.
            line = re.sub(r'[^\w\d\'\’\s]+', ' ', line)
            line = line.strip('\n')
            line = line.lower()

            # Splits the line of words separated by spaces into array.
            lineArray = line.split(' ')

            # Either increase the word's counter in dictionary or place
            #   the word in the dictionary along with initial value of 1.
            for word in lineArray:
                # This was done because there were whitespaces 'words' that
                #   ended up in the array in some test cases.
                if word.strip() == '':
                    pass
                elif word in wordDict:
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1
                    if maxWordLength < len(word):
                        maxWordLength = len(word)

    return wordDict, maxWordLength


def outputResult(inputFile, wordDict, justifyLength):

    # Appends each result to the output.txt file
    with open('output.txt', 'a', encoding='utf8') as f:
        print(inputFile, file=f)
        print('-' * 50, file=f)

        # Sorts the dictionary by value printing the largest value first.
        # The first print statement ensures that the lines are justified
        #   to the right bythe largest word found in the text file.
        for word in sorted(wordDict, key=wordDict.get, reverse=True):
            print(('{:>' + str(justifyLength) + '}').format(word),
                  file=f, end=' ')
            print('|', '=' * wordDict[word],
                  '(' + str(wordDict[word]) + ')', file=f)
        print('\n' * 2, file=f)


if __name__ == '__main__':

    # Removes the output.txt file if it exists (it will exist except the for
    #   the first time it is run).
    with contextlib.suppress(FileNotFoundError):
        os.remove('output.txt')

    # Reminds the user to provide file(s) to process if they forget.
    if len(sys.argv) == 1:
        print('When running, please list text the desired text file(s)',
              'after jobTest.py')

    # Processes all of the files and outputs them to one output.txt file.
    for x in range(1, len(sys.argv)):

        wordDict, justifyLength = processFile(sys.argv[x])

        outputResult(sys.argv[x], wordDict, justifyLength)
