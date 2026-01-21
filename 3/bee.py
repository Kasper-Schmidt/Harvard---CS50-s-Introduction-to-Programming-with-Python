WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")

        # TODO: Remove all if superword (Graphic) is guessed
        if guess == "GRAPHIC":
            WORDS.clear()
            print("You guessed the super word, you won!")

        # TODO: Check if guess in dictionary
        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job, you scored {points} points")

        



    print("That's the game!")


main()