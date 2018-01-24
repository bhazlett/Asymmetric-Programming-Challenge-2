from Candidate import Candidate
from AutocompleteProvider import AutocompleteProvider

def main():

    # This is the file given by the user it has the passages already written
    train_file = input("Please enter the name of the file you want to use to train: ")

    # This is the string entered by the user who wants some suggestions
    word = input("Please enter a word: ")

    # Builds the object and trains on the target file
    ACP = AutocompleteProvider()
    ACP.train(train_file)

    # Finds possbile words, sorts them, then dumps them
    print("Here are some suggestions")
    words = ACP.getWords(word)
    sorted_words = ACP.quicksort(words)
    ACP.dump(sorted_words)

main()
    
