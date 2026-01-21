import cowsay
import sys
import random

if len(sys.argv) != 2:
    sys.exit("Usage: python script.py name")

animal = random.choice(cowsay.char_names)
print(cowsay.cowsay("Hello, " + sys.argv[1], cow=animal))
