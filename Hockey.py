import json
class Hockey:
    def __init__(self):
        self.filename = ""

    def name_file(self):
        file = input("file name:")
        self.filename = file
        with open(self.filename) as my_file :
            data = json.load(my_file)
        
    
    def search_for_player(self):
        player_name = input("Name: ")
        with open(self.filename) as my_file:
            data = json.load(my_file)
        for player in data:
            if player_name == player["name"]:
                total = player["goals"] + player["assists"]
                print(f"{player['name']}        {player['nationality']}   {player['goals']} + {player['assists']} = {total}    ")
                break
            else : 
                print("No records found")
                break
    def teams(self):
        
        with open(self.filename) as my_file:
            data = json.load(my_file)
        nationalities = sorted(set(d["nationality"] for d in data))

        print("\n".join(nationalities))

    def countries(self):
        with open(self.filename) as my_file:
            data = json.load(my_file)
        countries  = sorted(set(d["team"] for d in data))

        print("\n".join(countries))


    def players_in_team(self):
        team_name = input("Team:")
        with open(self.filename) as my_file:
            data = json.load(my_file)
        players_in_given_team = [player for player in data if player["team"] == team_name]

        sorted_players = sorted(players_in_given_team, key=lambda player: player['goals'] + player['assists'], reverse=True)


        for player in sorted_players:
            total = player['goals'] + player['assists']
            print(f"{player['name']}      {player['team']}    {player['goals']} + {player['assists']}    {total}")

    def players_from_country(self):
        country_name = input("Country:")
        with open(self.filename) as my_file:
            data = json.load(my_file)
        players_in_given_team = [player for player in data if player["team"] == country_name]

        sorted_players = sorted(players_in_given_team, key=lambda player: player['goals'] + player['assists'], reverse=True)


        for player in sorted_players:
            total = player['goals'] + player['assists']
            print(f"{player['name']}      {player['team']}    {player['goals']} + {player['assists']}    {total}")

    def most_points(self):
        how_many = int(input("how many:"))
        with open(self.filename) as my_file:
            data = json.load(my_file)
        players = [player for player in data]
        result = sorted(players, key=lambda player : player['goals'] + player['assists'])
        print(result)
    def most_goals(self):
        pass 

    def help(self):
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def execute(self):
        self.name_file()
        self.help()
        while True: 
            command = input("command:")
            if command == '0':
                
                return False
                
            elif command == '1':
                self.search_for_player()
            elif command == '2':
                self.teams()
            elif command == '3':
                self.countries()
            elif command == '4':
                self.players_in_team()
            elif command == '5':
                self.players_from_country()
            elif command ==  '6':
                self.most_points()
            else: 
                self.most_goals()

hockey  = Hockey()
hockey.execute()





