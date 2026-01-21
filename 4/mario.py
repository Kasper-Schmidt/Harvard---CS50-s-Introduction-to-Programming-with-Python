def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        # DEBUG METODE: print(i, end=" "), sætter indeks på
        print("#" * (i + 1))


if __name__ == "__main__":
    main()