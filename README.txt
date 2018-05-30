David Toth's HEB Coding Challenge


How to run:

Python 3 must be installed to run this program.

To run with one file of input text:
python histogram.py input.txt

To run with multiple files of input text:
python histogram.py input.txt input2.txt input3.txt

All output will be sent to the same output.txt file and is labeled.


About the program:

The program will strip all punctuation excluding apostrophes (coded for utf-8
and apostrophes excluded are U+0027 ' and U+2019 ’).  All the words will then 
be processed in lower case for the sake of consistency and put into a 
dictionary.  The dictionary will keep track of key/value pairs of 
word/wordcount.  After the input.txt is processed the dictionary is sorted by 
value and the results written to output.txt.

The program does not account for hyphenated words.  This is because when 
looking for more test examples, I came across writing styles that used 
hypenated words as a means of transition.  I decided that unless I had a list 
of hyphenated words from the dictionary to include as an exception list I would 
remove all hyphens as punctuation.


Time Complexity:

To the best of my knowledge the processing of the file is O(n) where n is the 
number of words in the file as I only look at each word once when processing.  
However the sorting of the dictionary is O(nlog(n)), making the entire program 
this complexity.
