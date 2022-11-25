from guessNumber import guessNumber
from paperRockScissors import rps
from woordle import Woordle
from tictactoe import TicTacToe
from hangman import main

while True:
    txt = input("Welcome to the games app!!\n1.Guess the number\n2.Paper rock scissors\n3.Woordle\n4.TicTacToe\n5.Hangman\nPlease choose your game or press q for quit: ")
    if txt == '1':
        guessNumber()
    elif txt == '2':
        rps()
    elif txt == '3':
        game = Woordle()
        game.play()
    elif txt == '4':
        game = TicTacToe()
        game.play()
    elif txt == '5':
        main()
    elif txt == 'q':
        print("See you soon! Bye!")
        break