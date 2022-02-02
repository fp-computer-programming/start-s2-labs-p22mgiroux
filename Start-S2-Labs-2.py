# Author: MOG 2/2/22

last_initials = ["B", "D", "H", "E", "G", "G", "H", "R", "M", "L", "I", "I", "N", "N", "O", "P", "P", "X", "T", "S", "S", "P"]
rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin" "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]

def add_inital(rows, initials):
    position = 0
# For every index in each row, add the last initial followed by a periodto the first name in its origional "rows" list
    for i in range(len(rows)):
        for l in range(len(rows[i])):
            rows[i][l] += " {}.".format(initials[position])
# Advance the position of intitials list
            position +=1
# returned the converted names
    return rows

print(add_inital(rows, last_initials))