# Author: MOG 2/2/22

words = ["word", "dog", "piano", "red", "sweatshirt","running", "reviewing"]

def smash(lst):
# Empty str to contain "smashed" words
    sent = ""
# for every word, if the word isnt the last in the list, add it to sent with a space after it, if it is the last word, put a period at the end
    for word in lst:
        if word != lst[-1]:
            sent += word + " "
        else:
            sent += word + "."
# Print "smashed" words
    print(sent)

smash(words)