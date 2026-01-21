def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):        
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass                # kan også f.eks: print("x is not a integer")
    
main()




# funktion kan skrives, men flere linjer
'''
def get_int():        
    while True:
        try:
            x = int(input("What's x? "))
            return x    # return er stærkere end break, så den bryder også ud af loopet
        except ValueError:
            print("x is not a integer")    
'''



# Ikke i en funktion
'''
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not a integer")
    else:
        break

print(f"x is {x}")

'''








