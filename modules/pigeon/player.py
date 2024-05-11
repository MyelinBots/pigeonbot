startingPoints: int = 10000

class Player:
    def __init__(self, name: str):
        self.name = name
        self.points = startingPoints

    def name(self):
        return self.name

    def points(self):
        return self.points

    def changePoints(self, points: int):
        self.points += points

    def resetPoints(self):
        self.points = startingPoints

    def addPoints(self, points):
        self.points += points

    def removePoints(self, points):
        self.points -= points

    def __str__(self):
        return f"{self.name} has {self.points} points."
    
