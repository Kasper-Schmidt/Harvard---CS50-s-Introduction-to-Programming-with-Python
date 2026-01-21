def main():
    with open("alice.txt", "r") as f:
        contents = f.readlines()

    chapter1 = contents[52:272] # Jeg har ikke txt filen, men det er alt teskt i bogen, og kapitel 1 starter på 52 og slutter på 272
    with open("chapter1.txt", "w") as f:
        f.writelines(chapter1)

main()