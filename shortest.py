class Person:
    def __init__(self, name , height):
        self.name = name 
        self.height = height 


class Room :
    def __init__(self ):
        self.persons = []
    def add(self, person: Person):
        self.persons.append(person)
    def is_empty(self):
        if self.persons is None:
            return True
        else: 
            return False
    def print_contents(self):
        total_height = 0

        for person in self.persons :
            total_height += person.height
            print(f"{person}({person.height} cm )")
        print(f"There are {len(self.persons)} in the room , combined height is {total_height}")
room = Room()
print("Is the room empty?", room.is_empty())
room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Ally", 166))
room.add(Person("Nina", 162))
room.add(Person("Dorothy", 155))
print("Is the room empty?", room.is_empty())
room.print_contents()