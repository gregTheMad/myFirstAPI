import random

file_path = "C:/Users/macie/Downloads/sowpods.txt"

with open(file_path, "r") as file:
    words = file.read().splitlines()


hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def play_again():
    while True:
        game_screen = input("Play again? Y/N").upper()
        if game_screen == "Y":
            main()
            continue

        elif game_screen == "N":
            break

        else:
            break

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid imput")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already taken")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Win!")
            print(" ")
            is_running = False

        elif wrong_guesses >= (len(hangman_art) - 1):
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Lose!")
            print(" ")
            is_running = False

    play_again()

main()