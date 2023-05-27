#!/usr/bin/env python3

import random

def main():
    global parsed_words, wordcount, saved_words

    parsed_words = []
    wordcount = 0
    saved_words = []

    with open("dracula.txt", encoding="utf-8") as file:
        for line in file:
            words = line.split()
            parsed_words.extend(words)

    def first(wordcount):
        if wordcount < 1:
            print("Alright, first word - here we go!")
            random_word = str(random.choice(parsed_words))
            random_word = random_word.capitalize()
            selection = str(input(f"Does {random_word} make sense? (select y/n) "))
            if selection == "y":
                wordcount += 1
                saved_words.append(random_word)
                print(f"Excellent! {wordcount} word down.")
                middle(wordcount)
            else:
                print("Oops, let's try that again.")
                print(f"Reminder, {wordcount} words in our sentence.")
                first(wordcount)

    def middle(wordcount):
        if wordcount < 16:
            random_word = str(random.choice(parsed_words))
            selection = str(input(f"Does {random_word} make sense? (select y/n) "))
            if selection == "y":
                wordcount += 1
                saved_words.append(random_word)
                print(f"Excellent! {wordcount} words in our sentence now.")
                middle(wordcount)
            else:
                print("Oops, let's try that again.")
                print(f"Reminder, {wordcount} words in our sentence.")
                middle(wordcount)
        else:
            final(wordcount)

    def final(wordcount):
        if wordcount == 16:
            print("Okay, final word!")
            random_word = str(random.choice(parsed_words))
            selection = str(input(f"Does {random_word} make sense? (select y/n) "))
            if selection == "y":
                saved_words.append(random_word)
                delimiter = " "
                sentence = delimiter.join(saved_words)
                #print(wordcount)
                print(f"Congratulations! We did it! ")
                print(f"Our complete sentence is: {sentence}. \nThat was great fun! Thanks for playing!")
                quit()
            else:
                print("Oops, let's try that again.")
                print(f"Reminder, {wordcount} words in our sentence.")
                final(wordcount)

    print("Hello, dear user! I'm a super advanced LLM, so let's you and I write a sentence together! \nHere's how it'll work: ")
    print("1. I'll pull a random word from Bram Stoker's Dracula and display it on the screen. ")
    print("2. You select \"yes or no\" from the options \"y/n\", depending on whether that word makes sense in our sentence.")
    print("3. Once we get to 15 words (the average sentence length), I'll print out our sentence!")
    ready = str(input("Are you ready? (select y/n) "))

    if "y" in ready:
        first(wordcount)
    else:
        quit(wordcount)

# Call the main function
main()
