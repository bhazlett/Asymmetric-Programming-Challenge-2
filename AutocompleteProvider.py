# AutocompleteProvider.py
# Ben Hazlett
# 1/22/2018
# Description:
#   Written for the Asymmetric programming challenge. This file
#   contains a class written to count words from an incoming text
#   file then store those word counts in a dictionary.

from Candidate import Candidate

class AutocompleteProvider():

    # Constructor: inititalizes dictionaries to empty
    def __init__(self):
        # Word to candidate dictionary
        self.all_words = {}


    # quicksort()
    # Input: words (list of Candidates)
    # Output: words (list of Candidates)
    # Description:
    #   Implemenation of quicksort that uses extra lists to 
    #   sort the list. This version of sorting was used for the average
    #   big O time of O (n log n). 
    def quicksort(self, words):
        # Set up sub-lists
        less = []
        equal = []
        greater = []

        # If empty stop recursing
        if len(words) > 1:
            # Choose pivot from the end of the list
            pivot = words[len(words) - 1].getConfidence()

            # Iterate through the list
            for i in range(len(words)):
                
                # right of pivot
                if words[i].getConfidence() < pivot:
                    greater.append(words[i])
                # pivot wall
                if words[i].getConfidence() == pivot:
                    equal.append(words[i])
                # left of pivot
                if words[i].getConfidence() > pivot:
                    less.append(words[i])

            return self.quicksort(less)+equal+self.quicksort(greater)
        else:
            return words

        
    # train()
    # Input: filename (string)
    # Output: None (fills word_counts)
    # Description:
    #   1. Opens up the specified file
    #   2. Iterates through the file
    #   3. Calls the put_in_dict helper function to put the
    #      
    def train(self, filename):
        # Opens a target text file
        ifp = open(filename, "r")
        for line in ifp:
            words = line.split()
            # Puts each word in the line into the dictionary
            for word in words:
                self.putInDict(word.lower())
        ifp.close()

    # putInDict()
    # Input: word (string)
    # Output: fills word_counts with one word
    # Description:
    #    Checks if the word is already in word count 
    #    if it is adds one to the count. If not initializes
    #    that dictionary entry to a new candidate.
    def putInDict(self, word):
        # Checks if the word is already in the dict
        # if it is increase count by 1 if not
        # add a new Candidate object
        if word in self.all_words:
            self.all_words[word].increaseConfidenceByOne()
        else:
            self.all_words[word] = Candidate(word, 1)


    # getWords()
    # Input: fragment (string)
    # Output: words (list of Candidates)
    # Description: 
    #    Pulls all words that have the fragment as the starting charaters
    #    and returns them in a list.
    def getWords(self, fragment):
        words = []
        fragment = fragment.lower()
        # Find all words with the fragment as the beginning letters
        for word in self.all_words:
            if fragment == word[0:len(fragment)]:
                words.append(self.all_words[word])

        return words
              
    # dump()
    # Input: words (list of Candidates)
    # Output: None
    # Description:
    #   Goes through the words sent in and prints them using the Candidate
    #   stringify function
    def dump(self, words):
        count = 0
        end = len(words) - 1
        for i in range(len(words)):
            # used to make the output nice, no comma at the end
            if i != end:
                print(words[i].stringify(), end = ", ")
            else: 
                print(words[i].stringify())
        
