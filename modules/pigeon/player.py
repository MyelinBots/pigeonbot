startingPoints: int = 0

class Player:
    def __init__(self, name: str, startingPoints: int = startingPoints, startingCount: int = 0):
        self._name = name
        self._points = startingPoints
        self._count = startingCount

    def name(self) -> str:
        return self._name

    def points(self) -> int:
        return self._points

    def changePoints(self, points: int):
        self._points += points

    def resetPoints(self):
        self._points = startingPoints

    def addPoints(self, points):
        self._points += points

    def removePoints(self, points):
        self._points -= points
        if self._points < 0:
            self._points = 0

    def count(self):
        return self._count

    def __str__(self):
        return f"{self._name} has {self._points} points."
    
    def addCount(self):
        self._count += 1
    
