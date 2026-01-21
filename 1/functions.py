# defaulter toWho til world, hvis intet argument er givet. Ses med begge i slutningen
def main():
    name = input("What's your name? ")
    hello()
    hello(name)




def hello(toWho="World"):
    print(f"Hello", toWho)


main()