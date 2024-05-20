class Computer :
    def __init__(self, model , speed):
        self.model = model 
        self.speed = speed 
    
class LaptopComputer(Computer):
    def __init__(self,model, speed, weight):
        super().__init__(model, speed)
        self.weight = weight 

    def __str__(self):
        return f"{self.model},{self.speed},{self.weight}"
laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
print(laptop)