# Anagram Finder

## Usage

To initialize the Anagram Finder, navigate to the anagram folder containing `anagrams.py` and your input dictionary (a text file with a single dictionary entry on each line):
```
python3 anagrams.py <dictionary_file>
```

You may then enter words, and the program will print a list of anagrams of that word from the dictionary. Anagrams are case insensitive. A message "No anagrams found for word" will be printed if no anagram exists. 
Press enter exit to exit the program.

##  To install required dependencies for testing and coverage
```
pip3 install -r requirements.txt
``` 

## Design

Anagrams of two words should have the same exact representation, if we sort the words in them in lexigraphical order. 
The program process all the words by converting them to lowercase,then sorts characters within each word lexigraphically.
Finally groups words with the same lexigraphical sorting together (i.e. these words were anagrams of each other because they contain the same exact letters). 
These groupings are stored in a Trie, when reading input, the program will read each word, sort it and then insert it into a Trie belonging to an AnagramBase object. 
The  word's position in the Trie depends on its sorted self, but the actual word stored at the TrieNode is the original word. When we want to find a word and find its anagrams, we can convert the word to lowercase and sort the letters, and traverse down the AnagramBase's Trie.


Tries are usually a good choice when dealing with large amounts of data that can have redundant elements as well as searching for words. To find / insert a word in a BaseTrie, we must traverse `O(N)` nodes. Eventually, after the whole Trie is populated, the  list of words stored in each TrieNode is sorted as an additional post-processing that would make the online step quicker by avoiding the need to sort. Ideally, we can do this at runtime and cache because not every node will be used and we would do needless work, but the online runtime  will be slightly faster with this.

Also, the BaseTrie and TrieNode classes are generalized as much as possible so their usage could be essentially independent of our AnagramBase (i.e. we could use the BaseTrie and TrieNode classes for any other project with little modification).

## Run tests
Go to project root folder and run below command.
```
python3 -m pytest -v
```
## System requirements

Python3