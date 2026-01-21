# print("Hello, World")


'''
name = input("What's your name? ")
print("Hello", name)
print("Hello " + name)
'''


'''
name = input("What's your name? ")
print("Hello ", end="")
print(name)
'''


'''
name = input("What's your name? ")
print("Hello ", end="???")
print(name)
'''


# Print a quoteation mark --> single / double quotes
'''
print("Hello ", end="''")
print('Hello ', end='""')
'''


# \" med backslash foran quote, ser den det ikke som kode, men string
'''
print("Hello \"friend\"")
'''


'''
name = input("What's your name? ")
print(f"Hello {name}")
'''


# remove whitespace from string --> strip()
'''
name = input("What's your name? ")
name = name.strip()
print(f"Hello {name}")
'''


# remove whitespace from string til venstre og højre, 1 linje
'''
name = input("What's your name? ").strip()
print(f"Hello {name}")
'''


# stort forbogstav --> capitalize()
'''
name = input("What's your name? ").strip().capitalize()
print(f"Hello {name}")
'''


# strip og stort forbogstav --> strip() og upper()
'''
name = input("What's your name? ").strip().upper()
print(f"Hello {name}")
'''


# stort forbogstav i hvert ord/ navn --> title()
'''
name = input("What's your name? ").strip().title()
print(f"Hello {name}")
'''


# split input til fornavn og efternavn --> split(" ") <-- betyder jeg splitter ved mellemrum
'''
name = input("What's your name? ")
first, last = name.split(" ")
print(f"Hello {first}")
print(f"Hello {last}")
'''