# Dylan and Avi
# Fortune Cookie Generator
# Copyright 2018, Dylan Marchlinski and Avinesh Sriram

from random import choice
from os import system
from time import sleep

def filearr(fname):
    with open(fname) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    return lines

def fortune():
    pronoun = choice(filearr("words/Pronouns.txt"))
    adverb = choice(filearr("words/Adverbs.txt"))
    verb = choice(filearr("words/Verbs.txt"))
    noun = choice(filearr("words/Nouns.txt"))
    vowels = ["a", "e", "i", "o", "u"]
    clause = ""
    if noun[0] in vowels:
        clause = "an"
    else:
        clause = "a"
    system("clear")
    print("Your %s will %s %s %s %s." % (pronoun, adverb, verb, clause, noun))
    sleep(3)

def main():
    fortune()

main()
