#!/usr/bin/python3
import random


def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, "forenames.txt"),
                            (surnames, "surnames.txt")):
        with open(filename, encoding="utf8") as file:
            for name in file:
                names.append(name.rstrip())
    return forenames, surnames


forenames, surnames = get_forenames_and_surnames()
with open("test-names1.txt", "w", encoding="utf8") as file:
    for i in range(100):
        line = "{0} {1}\n".format(random.choice(forenames),
                                  random.choice(surnames))
        file.write(line)
