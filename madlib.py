#Name: Michael Jarvis
#Purpose: Develop a Python Program that uses file i/o. Practice processing string data. Practice function development. Creates a madlib with the user inputs.
#Authenticity: I made this program by myself at home.
#Last updated: 10/23/25

"""
Notes:
    Nouns = $
    Verbs = ^
    Adjectives = @
"""

from random import choice

#this function opens a file and reads the story then returns it as a single string
def read_story(filename):
    in_file = open(filename, "r")
    story = in_file.read()
    in_file.close()
    return story

#this function accepts the word type the user is looking for, asks the user to fill in the blanks for that word type, and then returns the user inputs as a list
#parameter choices: word_type = "noun", "verb", "adjective". story = "madlib.txt"
def get_words(word_type, story):
    #if the word type requested is a noun, the function goes through this loop
    if word_type == "noun":
        #empty list to store user inputed nouns later
        nouns = []
        #counts the number of nouns in the string
        noun_count = story.count("$")
        print("Number of nouns:", noun_count)
        #loop that asks the user for nouns equal to the number counted and stores them in the nouns_list, then returns that list
        for i in range(noun_count):
            user_noun = input("Enter a noun: ")
            nouns.append(user_noun)
        print("--------------------------------")
        return nouns
    #the next two elif statements mirror the if statement but work for verbs and adjectives
    elif word_type == "verb":
        verbs = []
        verb_count = story.count("^")
        print("Number of verbs:", verb_count)
        for i in range(verb_count):
            user_verb = input("Enter a verb: ")
            verbs.append(user_verb)
        print("--------------------------------")
        return verbs
    elif word_type == "adjective":
        adjectives = []
        adj_count = story.count("@")
        print("Number of adjectives:", adj_count)
        for i in range(adj_count):
            user_adj = input("Enter an adjective: ")
            adjectives.append(user_adj)
        print("--------------------------------")
        return adjectives

#this function brings in the story read by read_story(filename). It creates a new story using a blank string (new_story) and adding new nouns, verbs, and adjectives based on a random choice from the list generated during get_words. It then returns the new story.
def build_story(story, nouns, verbs, adjectives):
    new_story = ""
    #iterates through each character in the story string
    for word in story:
        #if the character in the string is a $ the string adds a new random noun from the list.
        if word == "$":
            new_story += choice(nouns)
        #if the character is not a $, and is a ^ the string adds a new random verb from the list.
        elif word == "^":
            new_story += choice(verbs)
        #if the character is not a $ or a ^, and is a @ the string adds a new random adjective from the list.
        elif word == "@":
            new_story += choice(adjectives)
        #if the character is none of the above options, it adds the already existing character.
        else:
            new_story += word
    return new_story

#this function opens a new file to write to, then writes the new story to it and closes the file.
def print_to_file(filename, story):
    out_file = open(filename, "w")
    out_file.write(story)
    out_file.close()

#main function gives mad lib intro text then runs all the functions in order, saving the results as new variables and inputing those variables in the following functions as parameters. It then gives instructions to open the output file.
def main():
   print("Let's build a mad lib!\n--------------------------------")
   story = read_story("madlib.txt")
   nouns = get_words("noun", story)
   verbs = get_words("verb", story)
   adjectives = get_words("adjective", story)
   new_story = build_story(story, nouns, verbs, adjectives)
   print_to_file("completed_mad_lib.txt", new_story)
   print("Open 'completed_mad_lib.txt' to read your mad lib!")

main()