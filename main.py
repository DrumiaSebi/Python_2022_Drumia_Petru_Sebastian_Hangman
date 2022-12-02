import random
from colorama import Fore
from colorama import Style


def chose_category():
    categories = ["Animale", "Copaci", "Imbracaminte, accesorii", "Mancare", "Meserii", "Parti ale corpului",
                  "Personalitati", "Sporturi", "Tari", "Transport"]
    print("You can get a word from the following categories:")
    for index, category in enumerate(categories):
        print("{0}: {1}".format(str(index+1), category))
    print()
    while True:
        chosen_category = input("Please enter the number for the category you want to chose: ")
        if chosen_category.isdigit() and 0 < int(chosen_category) <= len(categories):
            break
        else:
            print(f"{Fore.LIGHTRED_EX}Please select an existing category choosing the specific number!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}You will be given a random word from {Fore.LIGHTCYAN_EX}{categories[int(chosen_category)-1]}"
          f"{Fore.CYAN}!{Style.RESET_ALL}")
    return categories[int(chosen_category)-1]


def get_random_word(category):
    file = "Categories\\" + category + ".txt"
    with open(file, "r") as f:
        lines = f.readlines()
        line_index = random.randrange(len(lines))
        word = lines[line_index].strip()
        return word


def write_score(word, score):
    with open("score.txt", "a") as f:
        f.write(f"{word}, {score} \n")


def play_game(word):
    words = word.split(" ")
    guessed = ""
    for w in words:
        guessed += "_" * len(w) + "-"
    guessed = guessed[:len(guessed)-1]
    tries = len(word) // 2
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
        print(f"{Fore.RED}You failed! Better luck next time, the word was {Fore.LIGHTRED_EX}{word}{Fore.RED},you "
              f"had {Fore.LIGHTRED_EX}{failed_tries}{Fore.RED} attempts.{Style.RESET_ALL}")


play_game(get_random_word(chose_category()))


