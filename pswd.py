import random as r
import numpy as np
import csv


lower = "abcdefghijklmnopqrstuvwxyz "
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
numbers = "0123456789 "
all = lower + upper + numbers

# guessing password one character at a time
def oneChar(password):
    for x in password:
        found = False
        while(found == False):
            guesser = "".join(r.sample(all,1))
            count+=1
    
            if guesser == x:
                guess += guesser
                found = True
    print("attempts at hacking =", count)
    print("guess = " + guess)

# guessing password whole at a time
def fullGuess(password):
    found = False
    guess = ""
    count = 0
    guesses = []
    while(found == False):
        count += 1

        if password in guesses:
            for x in guesses:
                if x == password:
                    found = True
                    guess = x
        
        if password not in guesses:
            guesser = "".join(r.sample(all,len(password)))
            if guesser == password:
                found = True
                guess = guesser
            guesses.append(guesser)

    print("attempts at hacking =", count)
    print("guess = " + guess)

def readGuesses():
    guesses = []
    with open("guesses.csv") as file:
        lines = file.readline()
        for line in lines:
            line = line.replace('\n','')
            guesses += line.split(',')

def writeGuesses(guesses):
    with open("guesses.csv", 'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(guesses)