import sys
# argv -> argument vector -> en liste

# sys.exit, brug hvis programmet ikke skal andet end den ene ting. 

# terminal:
# python name.py Kasper
# python name.py "Kasper Schmidt"


if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])





'''
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])
'''





'''
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
'''





