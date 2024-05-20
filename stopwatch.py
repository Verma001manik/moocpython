class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):

        
        self.seconds += 1
        if(self.seconds > 59):
            if(self.minutes <= 59):

                self.minutes +=1
            else: 
                self.minutes = 0
            self.seconds = 0
        
        result = f"{self.minutes} : {self.seconds}"
        print(str(result))
watch = Stopwatch()
for i in range(3600):
    print(watch)
    watch.tick()