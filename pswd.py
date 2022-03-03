import random as r
import numpy as np
import csv


lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789 "
all = lower + upper + numbers

# guessing password one character at a time
def oneChar(password):
    count = 0
    guess = ""
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
    guesses = readGuesses()
    while(found == False):
        count += 1

        if password in guesses:
            for x in guesses:
                print(x, end='')
                print('\b' * len(x), end='', flush=True)
                if x == password:
                    found = True
                    guess = x
        elif password not in guesses:
                guesser = "".join(r.sample(all,len(password)))
                print(guesser, end='')
                print('\b' * len(guesser), end='', flush=True)
                if guesser == password:
                    found = True
                    guess = guesser
                guesses.append(guesser)
                

    print("attempts at hacking =", count)
    print("guess = " + guess)
    writeGuesses(guesses)

def readGuesses():
    guesses = []
    with open("guesses.csv") as file:
        lines = file.readline()
        lines = lines.replace('\n','')
        lines = lines.split(",")
    guesses = lines
    return guesses

def writeGuesses(guesses = []):
    with open("guesses.csv", 'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(guesses)