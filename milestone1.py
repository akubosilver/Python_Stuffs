#!/usr/bin/python3
"""
This is a simple tic-tac-toe game implimented in python

"""
#global variables
my_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
general_arr = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[0,4,8],[1,4,7],[2,5,8],[2,4,6]]
player1_arr = []
player2_arr = []
total_arr = []
#print game_board
def print_board(my_list):
    print(f'-----------------------------------------')
    print(f'      {my_list[0]}     |      {my_list[1]}        |     {my_list[2]}')
    print(f'            |               |              ')
    print(f'-----------------------------------------')
    print(f'            |               |              ')
    print(f'      {my_list[3]}     |      {my_list[4]}        |     {my_list[5]}')
    print(f'            |               |              ')
    print(f'-----------------------------------------')
    print(f'            |               |              ')
    print(f'      {my_list[6]}     |      {my_list[7]}        |     {my_list[8]}')
    print(f'-----------------------------------------')
#prompt player to select either 'X' or 'O'
def play(print_board,the_list):
    d = {'player1': '', 'player2': ''}
    while (d['player1']).upper() not in ['X', 'O']:
        d['player1'] = input("Please will you like to play as 'X' or 'O'? ")
    d['player1'] = (d['player1']).upper()
    if (d['player1']) == 'X':
        d['player2'] = 'O'
    else:
        d['player2'] = 'X'
    print(f'Player 1, You will be playing as {d["player1"]} and Player 2 as {d["player2"]}')
    start_game(print_board,d)   
#start game
def start_game(print_board,d):
    moves = 0
    player = ''
    answer = input(f'Shall we start the game?\nPlease enter "Y" or "N" ')
    if answer.lower() == 'y':
        while moves < 9:
            if moves%2==0:
                player = d['player1']
                players_position(print_board,player,moves)
                moves += 1
            else:
                player = d['player2']
                players_position(print_board,player,moves)
                moves += 1
    else:
        print("Good-Bye :( ")
        exit()
#prompt player to select position
def players_position(print_board,player,moves):
    position = ''
    while not position.isdigit() or int(position) not in range(1, 10) or int(position) - 1 in total_arr:
        position = input("Please enter your position from [1-9]: ")
    position = int(position) - 1
    total_arr.append(position)
    
    my_list[position] = player
    if moves:
        print('\n' * 100)
    print_board(my_list)
    update_game(moves, position)
#update game with players position
def update_game(moves,position):
    if moves >= 9:
        end_game()
    else:
        if moves%2==0:
            if len(player1_arr) < 3:
                player1_arr.append(position)
            elif len(player1_arr) == 3:
                player1_arr.pop(0)
                player1_arr.append(position)
            else:
                print("Error")
                exit()
        else:
            if len(player2_arr) < 3:
                player2_arr.append(position)
            elif len(player2_arr) == 3:
                player2_arr.pop(0)
                player2_arr.append(position)
            else:
                print("Error")
                exit()
    check_win(player1_arr,player2_arr)
#check for winner
def check_win(player1_arr,player2_arr):
    if len(total_arr) >= 9:
        print("Draw Game!!!")
        end_game()
    else:
        for items in general_arr:
            if set(items) == set(player1_arr):
                print("Player 1 Win!!!")
                end_game()
            elif set(items) == set(player2_arr):
                print("Player 2 Win!!!")
                end_game()
            else:
                pass
#end and restart function
def end_game():
    global my_list, total_arr, player1_arr, player2_arr
    my_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    total_arr, player1_arr, player2_arr = [], [], []
    replay = input("Will you like to play Again?\nEnter 'Y' for Yes or 'N' for No ")
    if replay.lower() == 'y':
        play(print_board,my_list)
    else:
        print("Good-Bye :(")
        exit()
#start game
play(print_board,my_list)