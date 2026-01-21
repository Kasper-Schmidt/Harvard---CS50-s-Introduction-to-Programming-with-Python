# Metode 2
def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print("#" * size)

main()




# metode 1
'''
def main():
    print_square(3)


def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("#", end="")

        # When done printing for the row, go to next line and print bricks
        print()

main()
'''




# metode 3
'''
def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):    
    print("#" * width)

main()
'''







# Vertical
'''
def main():
    print_column(3)

    
def print_column(height):
    for _ in range(height):
        print("#")

main()
'''

# Horizontal
'''
def main():
    print_row(4)


def print_row(width):
    print("#" * width)

main()
'''


