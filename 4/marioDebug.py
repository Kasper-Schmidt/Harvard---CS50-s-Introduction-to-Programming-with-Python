def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        print("#" * (i + 1)) # Ved at use debugger, siger den at i = 0 ved første gennemgang. Derfor skal det være (i + 1)


if __name__ == "__main__":
    main()