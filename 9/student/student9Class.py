# class --> blueprint for data/ objekter

class Student: 
    def __init__(self, name, house):     # instance method
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"     # dunder method
    

    # Getter function
    @property 
    def name(self):
        return self._name
    
    # Setter function
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name



    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    

def main():
    student = get_student()
    # student.house = "Number Four"     --- getter og setter gør så det fejler, hvis man prøver at snyde sig udenom ved at ændre den her til noget som ikke er en af de 4 huse
    # student._house = "Number Four"    --- ødelægger dog desværre, hvis man tilføjer _
    print(student)


def get_student():                 
    name = input("Name: ").title()
    house = input("House: ").title()
    return Student(name, house)  # Constructor
   


if __name__ == "__main__":
    main()