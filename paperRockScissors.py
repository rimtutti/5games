import random

def rps():
    print("---Let's play rock, paper, scissors---\n---To win the game, you have to take 3 victories---")
    choices = ["rock", "paper", "scissors"]
    userWin_counter = 0
    computerWin_counter = 0

    while computerWin_counter < 3 and userWin_counter < 3:
        computer_choice = random.choice(choices)
        user_choice = input("rock, paper, scissors?").strip().lower()
        
        if user_choice not in choices:
            print("Invalid selection")
            pass
        elif user_choice == computer_choice:
            print(f'{computer_choice} vs {user_choice}\n===DRAW===')
        elif user_choice == "rock":
            if computer_choice == "paper":
                print(f'{computer_choice} vs {user_choice}\n===YOU LOST===')
                computerWin_counter += 1
            else:
                print(f'{computer_choice} vs {user_choice}\n===YOU WON===')
                userWin_counter += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print(f'{computer_choice} vs {user_choice}\n===YOU WON===')
                userWin_counter += 1
            else:
                print(f'{computer_choice} vs {user_choice}\n===YOU LOST===')
                computerWin_counter += 1
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print(f'{computer_choice} vs {user_choice}\n===YOU LOST===')
                computerWin_counter += 1
            else:
                print(f'{computer_choice} vs {user_choice}\n===YOU WON===')
                userWin_counter += 1
        print(f'Result: COMPUTER: {computerWin_counter} YOU: {userWin_counter}')

    if userWin_counter == 3:
        print("===VICTORY===")
    else:
        print("===BETTER LUCK NEXT TIME===")






