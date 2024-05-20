class BallPlayer:
    def __init__(self, name, number, goals, assists, minutes):
        self.name = name
        self.number = number
        self.goals = goals
        self.assists = assists
        self.minutes = minutes
        self.points = self.goals + self.assists

    def __str__(self):
        return f"BallPlayer(name={self.name}, number={self.number}, goals={self.goals}, assists={self.assists}, minutes={self.minutes})"


def most_goals(items: list[BallPlayer]):
    return max(items, key=lambda item: item.goals)

def most_points(items: list[BallPlayer]):
    return max(items, key=lambda item: item.points)

def least_minutes(items: list[BallPlayer]):
    return min(items, key=lambda item: item.minutes)


if __name__ == "__main__":
    player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
    player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
    player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
    player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
    player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)

    team = [player1, player2, player3, player4, player5]
    print(most_goals(team))
    print(most_points(team))
    print(least_minutes(team))
