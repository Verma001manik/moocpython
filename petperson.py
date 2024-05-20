class Pet:
    def __init__(self, pet_name , breed):
        self.pet_name  = pet_name
        self.breed = breed
    

class Person:
    def __init__(self, person_name , pet: Pet):
        self.person_name = person_name
        self.pet = pet
    def __str__(self):
        return f"{self.person_name}, whose pal is {self.pet.pet_name}, {self.pet.breed}"


hulda = Pet("Hulda", "mixed-breed dog")
levi = Person("Levi", hulda)

print(levi)