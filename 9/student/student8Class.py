# class --> blueprint for data/ objekter

class Student: 
    def __init__(self, name, house, patronus):     # instance method
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"     # dunder method
    
    
    def charm(self):
        match self.patronus:
            case "Stag": 
                return "🐎"
            case "Otter":
                return "🦦"
            case "Dog":
                return "🐶"
            case _:
                return "🪄"


def main():
    student = get_student()
    print("Expecto Pretonus")
    print(student.charm())


def get_student():                 
    name = input("Name: ").title()
    house = input("House: ").title()
    patronus = input("Patrnous").title()
    return Student(name, house, patronus)  # Constructor
   


if __name__ == "__main__":
    main()