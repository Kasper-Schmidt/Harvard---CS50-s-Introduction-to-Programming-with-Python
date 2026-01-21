# class --> blueprint for data/ objekter

class Student: 
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()    # Laver et object ud fra classes                 
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()