class LotteryNumbers:
    def __init__(self, week: int, days: list):
        self.week = week
        self.days = days
    
    def number_of_hits(self,numbers:list):
        result = [number for number in numbers if self.days ==number]
        return result 
week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
my_numbers = [1,4,7,11,13,19,24]

print(week5.number_of_hits(my_numbers))