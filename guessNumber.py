import random

def guessNumber():
    print("---Let's play Guess the Number---\n---Guess the number from 1 to 100---")

    guesses = 0
    num = random.randint(1, 100)

    while True:
        n = int(input("Guess the number:"))
        guesses += 1

        if n == num:
            print(f"Great job, you found the number!\nNumber was: {num}\nNumber of guesses: {guesses}")
            break
        elif n > num:
            print("Too high!")
        elif n < num:
            print("Too low!")

