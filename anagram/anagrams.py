#!/usr/bin/python3
#################
# package imports
#################

import sys
import time


class AnagramBase:
    def __init__(self, input_filename):
        self.input_filename = input_filename
        self.word_trie = BaseTrie()
        self.read_input_words()

    # Reads words from an input file and inserts into word_trie.
    # Sorts word_trie in the end.
    def read_input_words(self):
        try:
            input_file = open(self.input_filename, "r")
        except IOError:
            print(f"{self.input_filename} is not a valid file.")
            sys.exit(9)
        for line in input_file:
            word = line.strip()
            sorted_word = "".join(sorted(word.lower()))
            self.word_trie.insert_into_trie(sorted_word, word)
        self.word_trie.sort_lists()

    # finds all anagrams of a given word
    def find_anagrams(self, word):
        sorted_word = "".join(sorted(word.lower()))
        return self.word_trie.find(sorted_word)


class BaseTrie:

    def __init__(self):
        self.top_node = TrieNode("")

    # inserts each word into the Trie
    def insert_into_trie(self, key, word):
        self.top_node.insert_word(key, word, -1)

    # Word's TrieNode is returned as a list of words or none if empty list
    def find(self, word):
        return self.top_node.find(word, -1)

    # sorts all lists of words in the Trie
    def sort_lists(self):
        self.top_node.sort_words()


class TrieNode:

    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.words = []

    # inserts given word into a TrieNode with position based on suffix, starting from index
    def insert_word(self, suffix, word, index):
        if len(suffix) == index + 1:
            self.words.append(word)
        else:
            first = suffix[index]
            if first not in self.children:
                self.children[first] = TrieNode(first)
            self.children[first].insert_word(suffix, word, index + 1)

    # looks for a given word in a TrieNode with position based on suffix, starting from index
    # returns words list at that TrieNode or empty list if not availabe
    def find(self, suffix, index):
        if len(suffix) == index + 1:
            return self.words
        elif suffix[index] in self.children:
            return self.children[suffix[index]].find(suffix, index + 1)
        else:
            return []

    # sorts the TrieNode's words, as well as its children's words
    def sort_words(self):
        self.words.sort()
        for child in self.children:
            self.children[child].sort_words()


def anagrams_finder(finder):
    '''Find anagram from finder object and return list of words comma separated
    If no anagrams found return No anagrams found for given input
    if input name is exit, exit out of program'''
    while True:
        test_word = input()
        if test_word == "":
            break
        elif test_word.lower().strip() == 'exit':
            sys.exit(0)
        else:
            anagrams_start_time = time.time()
            words = finder.find_anagrams(test_word)
            anagrams_end_time = time.time()
            time_took_in_ms = round((anagrams_end_time - anagrams_start_time) * 1000, 2)
            if not words:
                print (f"No anagrams found for {test_word} in {time_took_in_ms} ms")
            else:
                print (f"{len(words)} Anagrams found for {test_word} in {time_took_in_ms} ms")
                print(",".join(words))


def main():
    print("Welcome to the Anagram Finder \n-----------------------------")
    if len(sys.argv) == 2:
        input_filename = sys.argv[1]
    else:
        print("This script requires one input argument, please pass the name of dictionary file")
        sys.exit(1)
    # keep track of time taken to complete program
    start_time = time.time()
    # load Anagrams into trie
    finder = AnagramBase(input_filename)
    end_time = time.time()
    dictionary_load_time = round((end_time - start_time) * 1000, 2)
    print(f"Initialized in: {dictionary_load_time} ms.")
    anagrams_finder(finder)


if __name__ == "__main__":
    main()
