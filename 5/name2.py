import sys


if len(sys.argv) < 2:
    sys.exit("Too few arguments")


print("----------------")


for arg in sys.argv:
    print("Hello, my name is", arg)


print("----------------")


for arg in sys.argv[1:]: # Fjerner index 0, da det er name2.py
    print("Hello, my name is", arg)






