# Author: MOG 2/2/22

def double_every_other(lst):
# For every other index in the length of the string, double that index in place and return the final list
    for i in range(1,len(lst),2):
        lst[i] *= 2
    return lst