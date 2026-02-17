class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, Subject):
        super().__init__(name)
        self.Subject = Subject

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
Professor = Professor("Severus", "Defense Against the Dark Arts")
