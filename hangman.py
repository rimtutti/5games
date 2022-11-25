import random
from words import words

def target_word():
    word = random.choice(words)
    return word.upper()

def play(word):
    word_completion = '-' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("-------LET'S PLAY HANGMAN------")
    print(f"------{tries}/6 TRIES------")
    print(f'      {word_completion}')
    print("\n")

    while not guessed and tries > 0:
        guess = input('Enter a letter or word: ').upper()
        # Slucaj kada pogadjamo slovo
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You already guessed the letter', guess)
            elif guess not in word:
                print(guess, 'is not in the word.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f'Good job! {guess} is in the word!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:
                    guess = True
        # Slucaj kada pogadjamo rec
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You already guessed the word!', guess)
            elif guess != word:
                print(guess, 'is not the word.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Not valid guess!')
        print(f"------{tries}/6 TRIES------")
        print(f'      {word_completion}')

    if guessed:
        print('Congrats, you guessed the word!')
    else:
        print(f'You ran out of tries! The word was {word} .')

def main():
    word = target_word()
    play(word)
    while input('Play again? (Y/N)').upper() == 'Y':
        word = target_word()
        play(word)

if __name__ == '__main__':
    main()