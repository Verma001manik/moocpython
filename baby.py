class Person:
    def __init__(self, name: str,id: int,  height: int, weight : int):
        self.name = name
        self.id = id 

        self.height = height
        self.weight = weight



class BabyCentre:
    def __init__(self):
        self.weigh_in = 0
    def weigh(self, person: Person):
        self.weigh_in += 1 
        return person.weight


    def feed(self, person : Person):
        person.weight = person.weight+1
        return person.weight

    def weigh_ins(self):
        print(self.weigh_in)
baby_centre = BabyCentre()

eric = Person("Eric", 1, 110, 7)
peter = Person("Peter", 33, 176, 85)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

baby_centre.weigh(eric)
baby_centre.weigh(eric)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

baby_centre.weigh(eric)
baby_centre.weigh(eric)
baby_centre.weigh(eric)
baby_centre.weigh(eric)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")