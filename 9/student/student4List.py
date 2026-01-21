# List
# return [name, house] laver en liste (mutable -> kan ændres, vises med Padma)
# derfor kan du gøre student[1] = "Ravenclaw"

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name? ")
    house = input("House? ")
    return [name, house]


if __name__ == "__main__":
    main()
