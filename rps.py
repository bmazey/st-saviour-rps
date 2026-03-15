import random
import time

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print_dramatic_text('welcome to Mr. Mazey\'s rock, paper, scissors! 🗿📃✂️')

    score = 0
    options = ['🗿', '📃', '✂️']

    i = 0
    while i < 3:
        choice = ''
        while choice != 'rock' and choice != 'paper' and choice != 'scissors':
            choice = input('enter your choice (rock, paper, scissors): ')

        if choice == 'rock':
            choice = '🗿'
        if choice == 'paper':
            choice = '📃'
        if choice == 'scissors':
            choice = '✂️'

        opponent = options[random.randint(0, 2)]
        print_dramatic_text('rock ... paper ... scissors -- shoot! 💯')

        if choice == opponent:
            print(f'you chose {choice}  and opponent chose {opponent}  you tie!')
        if choice == '🗿' and opponent == '✂️':
            print(f'you chose {choice}  and opponent chose {opponent}  you win!')
            score += 1
        if choice == '🗿' and opponent == '📃':
            print(f'you chose {choice}  and opponent chose {opponent}  you lose!')
        if choice == '📃' and opponent == '🗿':
            print(f'you chose {choice}  and opponent chose {opponent}  you win!')
            score += 1
        if choice == '📃' and opponent == '✂️':
            print(f'you chose {choice}  and opponent chose {opponent}  you lose!')
        if choice == '✂️' and opponent == '📃':
            print(f'you chose {choice}  and opponent chose {opponent} you win!')
            score += 1
        if choice == '✂️' and opponent == '🗿':
            print(f'you chose {choice}  and opponent chose {opponent}  you lose!')
        
        i += 1

    print_dramatic_text(f'congratulations you scored {score}/3!')