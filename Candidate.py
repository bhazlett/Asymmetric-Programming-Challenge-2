# Candidate.py
# Ben Hazlett
# 1/22/2018
# Description:
#   Written for the Asymmetric programming challenge. This file
#   contains a class written to hold a word called a candidate

class Candidate():


    # Constructor: inititalizes dictionaries to empty
    def __init__(self, word, confidence):
        self.word = word
        self.confidence = confidence

    # get_confidence()
    # Input: word (string)
    # Output: confidence (int)
    def getConfidence(self):
        return self.confidence

    # get_word()
    # Input: word_frag (string)
    # Ouput: auto_complete (string)
    def getWord(self):
        return self.word

    # increase_confidence_by_1()
    # Input: None
    # Output: None
    def increaseConfidenceByOne(self):
        self.confidence += 1

    # stringify()
    # Input: None
    # Output: the information of the class (string)
    def stringify(self):
        return str(self.getWord() + " (" + str(self.getConfidence()) + ")")
        
