class Series :
    def __init__(self, title: str , seasons: int, genre: list):
        self.title = title
        self.seasons = seasons
        self.genre = [genre]
        self.total_rating = []
        self.average = 0
    # def total(self):
    #     return len(self.total_rating)
    def rate(self,rating: int):
        self.sum = 0
        self.total_rating.append(rating)
            
        return str(self.total_rating)
        
    def __str__(self):
        return f"{str(len(self.total_rating))} ratings"
    
    
dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
dexter.rate(4)
dexter.rate(5)
dexter.rate(5)
dexter.rate(3)
dexter.rate(0)
print(dexter)