import random
from rich import print


words = ("AUDIO", 
        "AULOI",
        "AUREI",
        "LOUIE"
        "MIAOU",
        "OUIJA",
        "OURIE",
        "URAEI")


class Woordle():
    def __init__(self):
        self.num_geusses = 0
        self.word = random.choice(words).lower()
        self.guess_dict = {
            0 : ["     "]*5,
            1 : ["     "]*5,
            2 : ["     "]*5,
            3 : ["     "]*5,
            4 : ["     "]*5,
            5 : ["     "]*5
        }
    
    def draw_boar(self):
        for guess in self.guess_dict.values():
            print(' | '.join(guess))
            print("=============================")

    def get_user_input(self):
        user_guess = input("Enter a 5 letter word: ")

        while len(user_guess) != 5:
            user_guess = input("Invalid input! Try again! 5 letters word!")

        user_guess = user_guess.lower().strip()

        for idx, char in enumerate(user_guess):
            if char in self.word:
                if char == self.word[idx]:
                    char = f"[green]{char}[/]" # green
                else:
                    char = f"[yellow]{char}[/]" # yellow
            self.guess_dict[self.num_geusses][idx] = char

        self.num_geusses += 1
        return user_guess

    def play(self):
        while True:
            self.draw_boar()
            user_guess = self.get_user_input()

            if user_guess == self.word:
                self.draw_boar()
                print(f'YOU WON!! The word was {self.word}')
                break

            if self.num_geusses > 5:
                self.draw_boar()
                print(f'YOU LOST!! The word was {self.word}')
                break