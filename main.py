import random
import sys

from colorama import Fore, Back, Style
import keyboard
import os


def chose_difficulty():
    global difficulties, selected_difficulty
    difficulties = ["easy", "medium", "hard"]
    selected_difficulty = 0

    def show_menu():
        global difficulties, selected_difficulty
        os.system('cls')
        print("Choose your difficulty:")
        for index, difficulty in enumerate(difficulties):
            if selected_difficulty == index:
                if selected_difficulty == 0:
                    print(Fore.BLACK + Back.LIGHTGREEN_EX + difficulty + Style.RESET_ALL)
                elif selected_difficulty == 1:
                    print(Fore.BLACK + Back.LIGHTYELLOW_EX + difficulty + Style.RESET_ALL)
                else:
                    print(Fore.BLACK + Back.LIGHTRED_EX + difficulty + Style.RESET_ALL)
            else:
                print(difficulty)

    def up():
        global selected_difficulty, difficulties
        selected_difficulty = (selected_difficulty - 1) % len(difficulties)
        show_menu()

    def down():
        global selected_difficulty, difficulties
        selected_difficulty = (selected_difficulty + 1) % len(difficulties)
        show_menu()
    show_menu()
    keyboard.add_hotkey('up', up)
    keyboard.add_hotkey('down', down)
    keyboard.wait("enter")
    return difficulties[selected_difficulty]


def chose_category():
    global categories, selected_category
    selected_category = 0
    categories = [category.split(".")[0] for category in os.listdir('Categories')]

    def show_menu():
        global categories, selected_category
        os.system('cls')
        print("What category you want your word to be from? Select from those below:")
        for index, category in enumerate(categories):
            if index == selected_category:
                print(f"{Fore.BLACK}{Back.BLUE}-> {category} <-{Style.RESET_ALL}")
            else:
                print(category)

    def up():
        global categories, selected_category
        selected_category = (selected_category - 1) % len(categories)
        show_menu()

    def down():
        global categories, selected_category
        selected_category = (selected_category + 1) % len(categories)
        show_menu()
    show_menu()
    keyboard.add_hotkey('up', up)
    keyboard.add_hotkey('down', down)
    keyboard.wait("enter")
    keyboard.remove_all_hotkeys()
    os.system('cls')
    print(f"You selected the category {Fore.LIGHTCYAN_EX}{categories[selected_category]}{Style.RESET_ALL}.")
    return categories[selected_category]


def get_random_word(category, difficulty):
    file = "Categories\\" + category + ".txt"
    try:
        with open(file, "r") as f:
            lines = f.readlines()
            hard_start_index = [index for index, line in enumerate(lines) if line.strip() == "HARD"]
            if difficulty == "hard":
                line_index = random.randrange(hard_start_index[0]+1, len(lines))
            else:
                line_index = random.randrange(hard_start_index[0]-1)
            word = lines[line_index].strip()
            return word
    except IOError as e:
        print("I/O operation error while trying to get a random word:" + str(e))
        sys.exit(1)
    except FileNotFoundError as e:
        print("File was not fount when trying to get a random word:" + str(e))
        sys.exit(1)


def write_score(word, score):
    try:
        with open("score.txt", "a") as f:
            f.write(f"{word}, {score} \n")
    except IOError as e:
        print("I/O operation error while trying to append current score to the score file:" + str(e))
        sys.exit(1)
    except FileNotFoundError as e:
        print("Score file was not found while trying to append to it:" + str(e))
        sys.exit(1)


def play_game(word, difficulty):
    words = word.split(" ")
    guessed = ""
    for w in words:
        guessed += "_" * len(w) + "-"
    guessed = guessed[:len(guessed)-1]
    if difficulty == "easy":
        tries = len(word)
    else:
        tries = len(word) // 2 + 1
    initial_tries = tries
    print(f"You have {Fore.LIGHTBLUE_EX}{tries} tries{Style.RESET_ALL} to guess the word, Good luck!")
    print(guessed)
    while tries != 0 and "_" in guessed:
        letter = input("Try and guess a letter: ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print(f"{Fore.LIGHTRED_EX}You can only give a single character as input!{Style.RESET_ALL}")
        elif letter in guessed.lower():
            print(f"{Fore.LIGHTRED_EX}This letter is in the word, you already guessed it!{Style.RESET_ALL}")
        else:
            letter_up = letter.upper()
            if letter_up in word or letter in word:
                positions_of_letter_up = [pos for pos, char in enumerate(word) if char == letter_up]
                for position in positions_of_letter_up:
                    guessed = guessed[:position] + letter_up + guessed[position + 1:]
                positions_of_letter = [pos for pos, char in enumerate(word) if char == letter]
                for position in positions_of_letter:
                    guessed = guessed[:position] + letter + guessed[position+1:]
                print(guessed)
            else:
                tries -= 1
                if tries == 1:
                    print(f"The given letter is not in the word,{Fore.LIGHTRED_EX} this is your last try!{Style.RESET_ALL}")
                elif tries < 4:
                    print(f"The given letter is not in the word,{Fore.RED} you have {tries} tries left!{Style.RESET_ALL}")
                elif tries < 6:
                    print(f"The given letter is not in the word,{Fore.LIGHTYELLOW_EX} you have {tries} tries left!{Style.RESET_ALL}")
                else:
                    print(f"The given letter is not in the word,{Fore.LIGHTBLUE_EX} you have {tries} tries left!{Style.RESET_ALL}")
                print(guessed)
    failed_tries = initial_tries - tries
    if tries > 0:
        print(f"{Fore.CYAN} Congratulations, you guessed the word: {Fore.LIGHTCYAN_EX}{word}{Fore.CYAN}! with "
              f"{Fore.LIGHTCYAN_EX}{failed_tries}{Fore.CYAN} tries.{Style.RESET_ALL}")
        write_score(word, failed_tries)
    else:
        print(f"{Fore.RED}You failed! Better luck next time, the word was {Fore.LIGHTYELLOW_EX}{word}{Fore.RED},you "
              f"had {Fore.LIGHTYELLOW_EX}{failed_tries}{Fore.RED} attempts.{Style.RESET_ALL}")


difficulty = chose_difficulty()
category = chose_category()
play_game(get_random_word(category, difficulty), difficulty)












