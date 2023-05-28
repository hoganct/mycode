#!/usr/bin/env python3

# importing libraries
import random
import requests

books_dict = {"1":"cache/epub/1513/pg1513.txt", "2":"files/2701/2701-0.txt", "3":"cache/epub/2641/pg2641.txt", 
         "4":"cache/epub/145/pg145.txt", "5":"cache/epub/37106/pg37106.txt", "6":"cache/epub/1342/pg1342.txt",
         "7":"cache/epub/11/pg11.txt", "8":"cache/epub/2600/pg2600.txt", "9":"files/1661/1661-0.txt",
         "10":"cache/epub/6130/pg6130.txt"}

books_list = ["blank", "1. Romeo & Juliet, by William Shakespeare",
"2. Moby Dick, by Herman Melville",
"3. A Room With A View, by E.M. Forster",
"4. Middlemarch, by George Eliot",
"5. Little Women, by Louisa May Alcott",
"6. Pride and Prejudice, by Jane Austen",
"7. Alice's Adventures in Wonderland, by Lewis Carroll",
"8. War and Peace, by Leo Tolstoy",
"9. The Adventures of Sherlock Holmes, by Sir Arthur Conan Doyle",
"10. The Iliad, by Homer"]

books_url_keys = list(books_dict)

# defining main, to be invoked at starting user prompt
def main():
    global parsed_words, wordcount, saved_words, book_selection, book_dict_value, appended_url # defining these as global variables

    book_selection = "" # declare the book_selection variable
    book_dict_value = "" # declare the book_dict_value variable
    appended_url = "" # declaring the appended URL for later use

    parsed_words = [] # empty list
    wordcount = 0 # counter
    saved_words = str("blank") # to compile into sentence

    # defining a reader function, to take the appended url and make a request from the value from user input
    def reader(appended_url): # passing appended_url as the argument
        try:
            response = requests.get(appended_url) # passing appended URL to requests
            response.raise_for_status() # raising exception for error
            content = response.text # converting the content to text
        except requests.exceptions.RequestException as e: # need except for failed try
            print("Error:", e)
        lines = content.splitlines() # splitting lines in content, the text file of the book
        for line in lines: 
            words = line.split() # splitting lines into words
            parsed_words.extend(words) # extending parsed_words list by words
        first(wordcount) # going to first

    def first(wordcount): # defining function for the first iteration, with wordcount as the argument
        global saved_words
        
        if wordcount < 1:
            print("Alright, first word - here we go!")
            random_word = str(random.choice(parsed_words)) # using random to select choice from list
            random_word = random_word.capitalize() # capitalizing the first letter, since it's the first word
            selection = str(input(f"Does \"{random_word}\" make sense? (select y/n) ")) # prompting user input to determine loop conditional
            if selection == "y":
                wordcount += 1 # add to the counter
                saved_words = str(random_word) + " " # save the random word to "saved_words"
                print(f"Excellent! {wordcount} word down.") # give the user a pat on the back
                middle(wordcount) # pass user to middle() with the wordcount variable in tow
            else:
                print("Oops, let's try that again.")
                first(wordcount) # going back to the beginning

    def middle(wordcount):
        global saved_words
        
        if wordcount < 16: # doing this for the next 15 or so
            random_word = str(random.choice(parsed_words)) # next few lines same as above
            random_word = random_word.lower() # forcing lowercase on this word
            print(f"Here's what you have so far: {saved_words}")
            selection = str(input(f"Does \"{random_word}\" make sense? (select y/n) "))
            if selection == "y":
                wordcount += 1
                saved_words = saved_words + random_word + " "
                print(f"Excellent! {wordcount} words in our sentence now.")
                middle(wordcount) # going back to the top, with the wordcount variable with us
            else:
                print("Oops, let's try that again.")
                print(f"Reminder, {wordcount} words in our sentence.")
                middle(wordcount) # keeping it in middle()
        else:
            final(wordcount) # all other values, take it to final()

    def final(wordcount):
        global saved_words
        
        if wordcount == 16:
            random_word = str(random.choice(parsed_words))
            random_word = random_word.lower()
            print("Okay, final word!") # all the same stuff here
            print(f"Here's what we have so far: {saved_words}")
            selection = str(input(f"Does \"{random_word}\" make sense? (select y/n) "))
            if selection == "y":
                saved_words = saved_words + random_word
                print(f"Congratulations! We successfully made a sentence by {title_author}!")
                print(f"Our complete sentence is: {saved_words}. \nThat was great fun! Thanks for playing!") # printing out the whole sentence
                quit() # exit the whole program - we're done!
            else:
                print("Oops, let's try that again.")
                print(f"Reminder, {wordcount} words in our sentence.")
                final(wordcount)

    print("Hello, dear user! I'm a super advanced LLM, so let's you and I write a sentence together! \nHere's how it'll work: ") # text instructions for our dear user
    print("1. I'll pull a random word from a book we'll choose together and display it on the screen. ")
    print("2. You select \"yes or no\" from the options \"y/n\", depending on whether that word makes sense in our sentence.")
    print("3. Once we get to 17 words (the average sentence length), I'll print out our sentence!")
    ready = str(input("Are you ready? (select y/n) ")) # storing the user input in the ready variable, to be checked below

    if ready == "y": # using this to invoke runtime
        print(f"Okay here are the options:")
        for book in books_list:
            print(book) # printing out all the options
        book_selection = str(input(f"Which one would you like to work with? \n{books_url_keys} \n")) # giving the user an option based on keys in dictionary, 1-10
        book_dict_value = books_dict[book_selection] # taking the user input key (1-10) to return a value, to later add to url
        books_list_selection = books_list[int(book_selection)] # working with just the titles and authors
        if "10." in books_list_selection: # if it's #10, then drop the first 4 characters and save to title_author - just pretty printing
            title_author = books_list_selection[4:]
        else: # otherwise, drop first 3 and do the same
            title_author = books_list_selection[3:]
        if book_dict_value is not None:
            print(f"Excellent! You chose {title_author}!")
            appended_url = ("https://www.gutenberg.org/" + book_dict_value) # appending the value to gutenberg url
            reader(appended_url) # calling reader, with appended_url as an argument
        else:
            print("Invalid book selection, exiting...")
    else:
        print("Exiting...")
        quit() # all others, quit the program

# call the main function
main()
