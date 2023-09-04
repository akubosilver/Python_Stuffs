from random import shuffle
my_list = ['0', ' ', ' ']
def shuffle_func(my_list):
    shuffle(my_list)
    return my_list

def players_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Please enter 0, 1, or 2! ")
    return int(guess)

def check_guess(my_list, guess):
    if my_list[guess] == '0':
        print("Correct Guess!!!")
        print(my_list)
        answer = input("Will you like to continue? ")
        if answer.lower() == "yes":
            start_game()
        else:
            pass
    else:
        print("Wrong Guess!!!\nTry Again")
        start_game()

def start_game():
    new_list = shuffle_func(my_list)
    guess = players_guess()
    check_guess(new_list,guess)

start_game()