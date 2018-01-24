from Candidate import Candidate
from AutocompleteProvider import AutocompleteProvider

def main():
    
    # Number of files expected
    number_of_files = int(input("How many files are being input: "))

    # Makes the object
    ACP = AutocompleteProvider()

    for i in range(number_of_files):

        # This is the file given by the user it has the passages already written
        train_file = input("Please enter the name of the file you want to use to train: ")

        # This is the string entered by the user who wants some suggestions
        word = input("Please enter a word: ")

        # trains on the target file
        ACP.train(train_file)

        # Finds possbile words, sorts them, then dumps them
        print("Here are some suggestions after one file")
        words = ACP.getWords(word)
        sorted_words = ACP.quicksort(words)
        ACP.dump(sorted_words)
    
main()
    
