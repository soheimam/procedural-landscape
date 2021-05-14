import random
from termcolor import colored
from noise import pnoise2


def generate_land(rows=4, cols=4):

    data = ["@", "c", "&", "e", "f", "f", "e", "&", "c", "@"]
    seed = random.randint(0, 100)
    land = " "
    print("generate land...")

    for row in range(rows):
        for col in range(cols):
            n = pnoise2(row / rows, col / cols, base=seed)
            n *= 10
            n = round(n)
            n = n % len(data)
            land += data[n]
        land += "\n"
    return land


def ask_for_number(question):
    tries = 0

    while tries < 3:
        answer = input(question + " ")

        if answer == "quit":
            quit()
        if answer.isnumeric():
            return int(answer)
        else:
            print(colored('oops enter a number', 'red'))
            tries += 1
    quit()


if __name__ == "__main__:":
    rows = ask_for_number("How many rows?")
    cols = ask_for_number("How many cols?")

    output = generate_land(rows, cols)
    print(output)
