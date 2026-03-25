import random
import time

def print_dramatic_text(text: str, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print_dramatic_text('welcome to rock, paper, scissors! 🗿📃✂️')

    options = ['rock', 'paper', 'scissors']
    choice = random.randint(0, 2)

    computer = options[choice]

    print('computer player selected: ' + options[choice])

    response = input('please choose rock, paper, or scissors: ')

    while response != 'rock' and response != 'paper' and response != 'scissors':
        response = input('please choose rock, paper, or scissors: ')

    print(f'player selected {response}')

    if response == 'rock' and computer == 'rock':
        print('you tie!')
    if response == 'rock' and computer == 'scissors':
        print('you win!')
    if response == 'rock' and computer == 'paper':
        print('you lose!')
