class Wizard:
    def __init__(self, name, patronus):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.patronus = patronus



class Student(Wizard):
    def __init__(self, name, house, patronus):
        super().__init__(name)
        self.house = house
        super().__init__(patronus)

    ...


class Professor(Wizard):
    def __init__(self, name, subjects, patronus):
        super().__init__(name)
        self.subjects = subjects
        super().__init__(patronus)

    ...


wizard = Wizard("Albus", "Phoenix")
student = Student("Harry", "Gryffindor", "Stag")
professor = Professor("Severus", "Defence against the Dark Arts", "Doe")

