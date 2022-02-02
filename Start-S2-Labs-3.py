# Author: MOG 2/2/22

def comes_after(st, l): 
# empty string for result
    string = ""
# for every element in the list made out of the string, if it isnt the last element, if it is the letter we are given, and the next letter is in the alphabet, add it to the string
    for i, x in enumerate(list(st)):
        if i != len(st) - 1:
            if x.lower() == l.lower() and st[i+1].isalpha():
                string += st[i+1]
    return string