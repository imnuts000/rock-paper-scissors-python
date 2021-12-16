import rps
import ctypes
from art import *

tprint('Rock-Paper-Scissors')
print("by nosferatu.bodya")

while True:
    p_move = input("\nEnter you move ('rock', 'paper', 'scissors') or 'exit' to exit: ")
    if(p_move == "exit"):
        break
    elif not(p_move in rps.actions):
        print("Wrong command")
        continue
    e_move = rps.enemy_move()
    rps.check_winner(p_move, e_move)