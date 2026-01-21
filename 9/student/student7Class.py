# class --> blueprint for data/ objekter

class Student: 
    def __init__(self, name, house):     # instance method
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():                 
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)  # Constructor
   


if __name__ == "__main__":
    main()