class ComputerGame:
    def __init__(self, name , owner , year):
        self.name = name 
        self.owner = owner 
        self.year = year 
class GameWarehouse:
    def __init__(self):
        self.list = []
    
    def add_game(self, game : ComputerGame):
        self.list.append(game)
    def list_games(self):
        return self.list

class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def list_games(self):
        new_list = []
        for game in super().list_games():
            if game.year <1990:
                new_list.append(game)
        return new_list



museum = GameMuseum()
museum.add_game(ComputerGame("Pacman", "Namco", 1980))
museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))
for game in museum.list_games():
    print(game.name)