def main():

    difficulty = input("Difficult or Casual?")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return

    players = input("Multiplayer or Single-player?")
    if not (players == "Multiplayer" or players == "Single-plyer"):
        print("Enter a valid number of players")
        return
    
    if difficulty == "difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")
        



def recommend(game):
    print("You might like", game)



main()


'''
def main():
    difficulty = input("Difficult or casual?")
    players = input("Multiplayer or Single-player?")
    
    if difficulty == "difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Klondike")
        else:
            print("Enter a valid number of players")
    elif difficulty == "casual":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single-player":
            recommend("Clock")
        else:
            print("Enter a valid number of players")
    else:
        print("Enter a valid difficulty")



def recommend(game):
    print("You might like", game)



main()
'''