class Person:
    count_id = 0

    def __init__(self, name , surname ):
        self.name  = name
        self.surname = surname
        self.id = self.get_next_id ()

    @staticmethod
    def get_next_id():
        Person.count_id += 1
        next_id = Person.count_id
        return next_id


    def __add__(self, other):
        return f"{self.name} {other.surname}"

    def __repr__(self):
        return f"Person {self.id}: {self.name} {self.surname}"

    def __str__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name , people ):
        self.name  = name
        self.people  = people

    def __add__(self, other):
        return self.people + other.people

    def __len__(self):
        return len(self.people)

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index]}"


    def __str__(self):
        members = ", ".join ( str(p) for p in self.people )
        return f"Group {self.name} with members {members}"

