# int
'''
x = input("What is x? ")
y = input("What is y? ")

z = int(x) + int(y)
print(z)
'''

# Bedre - mere simpel
'''
x = int(input("What is x? "))
y = int(input("What is y? "))

print(x + y)
'''



#float 
'''
x = float(input("What is x? "))
y = float(input("What is y? "))

print(x + y)
'''


# round() --> round(number[, ndigits])
'''
x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x + y)

print(z)
'''

# komma efter hver tredje, så der f.eks. står 1,000
'''
x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x + y)

print(f"{z:,}")
'''


# Dansk tusindtalsseperator: .
'''
# Dansk tusindstalsseperator
x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x + y)

print(f"{z:,}".replace(",", "."))
'''


# dividere
'''
x = float(input("What is x? "))
y = float(input("What is y? "))

z = x / y

print(z)
'''


# Dividere & round til 2 decimaler
'''
x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x / y, 2)

print(z)
'''



# 2 decimaler med f-string
'''
x = float(input("What is x? "))
y = float(input("What is y? "))

z = x / y

print(f"{z:.2f}")
'''



















