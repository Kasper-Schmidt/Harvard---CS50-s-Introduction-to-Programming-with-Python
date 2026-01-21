import random

cards = ["K", "Q", "J"]

def main():
    random.seed(0) # fast tal: altid samme resultat, ved det tal, sæt seed til 1, er svaret noget andet, men altid det samme

    print(random.choice(cards))
    print(random.choices(cards, k=2)) 
    print(random.choices(cards, weights=[50, 25, 25], k=2)) # Del 100% ud til hver 
    
    print(random.sample(cards, k=2)) # sample tager kortet ud efter det er valgt og fortsætter med resten
    
    


main()