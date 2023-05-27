#!/usr/bin/env python3

# importing libraries
import random

# defining main, to be invoked at starting user prompt
def main():
    global parsed_words, wordcount, saved_words # defining these as global variables

    parsed_words = [] # empty list
    wordcount = 0 # counter
    saved_words = [] # to compile into sentence

    with open("dracula.txt", encoding="utf-8") as file: # parsing out all the words in dracula into a list; the file is available from here (https://www.gutenberg.org/files/345/345-0.txt), but any .txt file will work
        for line in file:
            words = line.split()
            parsed_words.extend(words)

    def first(wordcount): # defining a function for the first iteration
        if wordcount < 1:
            print("Alright, first word - here we go!")
            random_word = str(random.choice(parsed_words)) # using random to select choice from list
            random_word = random_word.capitalize() # capitalizing the first letter, since it's the first word
            selection = str(input(f"Does {random_word} make sense? (select y/n) ")) # prompting user input to determine loop conditional
            if selection == "y":
                wordcount += 1 # add to the counter
                saved_words.append(random_word) # save the word to list "saved_words"
                print(f"Excellent! {wordcount} word down.") # give the user a pat on the back
                middle(wordcount) # pass user to middle() with the wordcount variable in tow
            else:
                print("Oops, let's try that again.")
                print(f"Reminder, {wordcount} words in our sentence.")
                first(wordcount) # going back to the beginning

    def middle(wordcount):
        if wordcount < 16: # doing this for the next 15 or so
            random_word = str(random.choice(parsed_words)) # next few lines same as above
            selection = str(input(f"Does {random_word} make sense? (select y/n) "))
            if selection == "y":
                wordcount += 1
                saved_words.append(random_word)
                print(f"Excellent! {wordcount} words in our sentence now.")
                middle(wordcount) # going back to the top, with the wordcount variable with us
            else:
                print("Oops, let's try that again.")
                print(f"Reminder, {wordcount} words in our sentence.")
                middle(wordcount) # keeping it in the middle
        else:
            final(wordcount) # all other values, take it to final()

    def final(wordcount):
        if wordcount == 16:
            print("Okay, final word!") # all the same stuff here
            random_word = str(random.choice(parsed_words))
            selection = str(input(f"Does {random_word} make sense? (select y/n) "))
            if selection == "y":
                saved_words.append(random_word)
                delimiter = " " # defining the delimiter as a space
                sentence = delimiter.join(saved_words) # joining the list to make it a string
                print(f"Congratulations! We did it! ")
                print(f"Our complete sentence is: {sentence}. \nThat was great fun! Thanks for playing!") # printing out the whole sentence
                quit() # exit the whole program - we're done!
            else:
                print("Oops, let's try that again.")
                print(f"Reminder, {wordcount} words in our sentence.")
                final(wordcount)

    print("Hello, dear user! I'm a super advanced LLM, so let's you and I write a sentence together! \nHere's how it'll work: ") # text instructions for our dear user
    print("1. I'll pull a random word from Bram Stoker's Dracula and display it on the screen. ")
    print("2. You select \"yes or no\" from the options \"y/n\", depending on whether that word makes sense in our sentence.")
    print("3. Once we get to 17 words (the average sentence length), I'll print out our sentence!")
    ready = str(input("Are you ready? (select y/n) ")) # storing the user input in the ready variable, to be checked below

    if "y" in ready: # using this to invoke runtime
        first(wordcount) # if yes, take me to first()
    else:
        quit(wordcount) # all others, quit the program

# call the main function
main()
