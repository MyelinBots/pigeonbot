from .actions import Action
from .player import Player
from .timer import RepeatedTimer
import random
class Game:
    def __init__(self, irc):
        self.irc = irc
        self.players: [Player] = []
        self.actions: [Action] = [
            Action("stole", ["tv", "wallet", "food"], "a pigeon %s your %s", 10),
            Action("pooped", ["car", "table", "head"], "a pigeon %s on your %s", 10),
            Action("landed", ["balcony", "head", "car", "house"], "a pigeon has %s on your %s", 10),
        ]

    def addPlayer(self, name: str) -> None:
        for player in self.players:
            if player.name == name:
                return
        self.players.append(Player(name))

    def findPlayer(self, name: str):
        for player in self.players:
            if player.name() == name:
                return player  


    def removePlayer(self, name: str) -> None:
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
                return

    def actOnPlayer(self) -> None:
        print("Going to trigger pigeon attack")
        print(len(self.players))
        if len(self.players) == 0:
            print("No players to act on")
            return
        player = random.choice(self.players)
        action = random.choice(self.actions)
        # player.changePoints(action.actionPoint)
        self.irc.privmsg(self.irc.config.channel,  action.act())

    def start(self):
        print("dones something")
        # do interval for every 5 seconds
        RepeatedTimer(10, self.actOnPlayer)

    def attemptShoot(self, nick):
        player = self.findPlayer(nick)
        shot = random.choice([True,False])
        if shot:
            player.addPoints(10)
            


