import random

actions = ['rock', 'paper', 'scissors']
action_weight = {'rock': 0, 'paper': 1, 'scissors': 2}
p_win_msg = "Player won"
e_win_msg = "You lost"
d_msg = "Draw"

def enemy_move():
    num = random.randint(0, 2)
    print(f"enemy move: {actions[num]}")
    return actions[num]

def check_winner(p_move: str, e_move: str):
    if(action_weight[p_move] == action_weight[e_move]):
        print(d_msg)
    elif (p_move == "rock"):
        if e_move == "paper":
            print(e_win_msg)
        elif e_move == "scissors":
            print(p_win_msg)
    elif p_move == "paper":
        if e_move == "rock":
            print(p_win_msg)
        elif e_move == "scissors":
            print(e_win_msg)
    elif p_move == "scissors":
        if e_move == "rock":
            print(e_win_msg)
        elif e_move == "paper":
            print(p_win_msg)