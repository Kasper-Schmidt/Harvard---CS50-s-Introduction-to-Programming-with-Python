# Tuple
# return name, house laver en tuple (immutable)
# student[0], student[1] = tuple-indeks

def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name? ")
    house = input("House? ")
    return name, house


if __name__ == "__main__":
    main()
