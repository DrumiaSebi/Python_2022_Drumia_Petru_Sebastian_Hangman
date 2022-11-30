import random
def chose_category():
    categories = ["Animale", "Copaci", "Imbracaminte, accesorii", "Mancare", "Meserii", "Parti ale corpului",
                  "Personalitati", "Sporturi", "Tari", "Transport"]
    print("Please chose the category you would like your word to be from:")
    for index, category in enumerate(categories):
        print("{0}: {1}".format(str(index+1), category))
    print()
    chosen_category = int(input("Please enter the number for the category you want to chose: "))
    return categories[chosen_category-1]


def get_random_word(category):
    file = "Categories\\" + category + ".txt"
    with open(file, "r") as f:
        lines = f.readlines()
        line_index = random.randrange(len(lines))
        word = lines[line_index].strip()
        print(word)
        return word


# def play_game(word):
#     guessed = "_" * len(word)
#     tries = len(word) // 2
#     while tries != 0:
#         letter = input("Try and guess a letter: ")
#         if letter in word:
#             positions_of_letter = [pos for pos, char in enumerate(word) if char == letter]
#             for position in positions_of_letter:
#                 guessed[position] = letter
#                 print(guessed)
#         else:
#             print("Letter not in word")
#             tries -= 1
#             print("Tries left: {0}".format(tries))
    # print(guessed)


# get_random_word("Personalitati")
# play_game(get_random_word("Personalitati"))


