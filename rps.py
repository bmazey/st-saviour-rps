import random
import time

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print_dramatic_text('welcome to Mr. Mazey\'s rock, paper, scissors! 🪨📃✂️')

    score = 0
    options = ['rock', 'paper', 'scissors']

    i = 0
    while i < 3:
        choice = ''
        while choice != 'rock' or choice != 'paper' or choice != 'scissors':
            choice = input('enter your choice (rock, paper, scissors): ')

        opponent = options[random.randint(0, 2)]
        print_dramatic_text('rock ... paper ... scissors ... shoot!')

