import os

from .actions import Action
from .config import Config
from .player import Player
from .timer import RepeatedTimer
from .pigeon import Pigeon, pigeons
import random


class Game:
    def __init__(self, irc):
        self._config = Config(interval=os.environ.get("PIGEON_INTERVAL", 5))
        self.irc = irc
        self.players: [Player] = []
        self.actions: [Action] = [
            Action("stole", ["tv", "wallet", "food", "girlfriend/boyfriend", "phone", "ice cream", "laptop", "sandwich", "cookie", "headphones", "keyboard"], "A %s pigeon %s your %s", 10),
            Action("pooped", ["car", "table", "head", "laptop", "bed", "shoes", "shirt", "phone", "couch", "carpet", "pants"], "A %s pigeon %s on your %s", 10),
            Action("landed", ["balcony", "head", "car", "house", "swimming pool", "bed", "couch", "table"], "A %s pigeon has %s on your %s", 10),
        ]
        self.active: Pigeon = None
        self.pigeons: [Pigeon] = pigeons


    def addPlayer(self, name: str) -> None:
        for player in self.players:
            if player.name == name:
                return
        self.players.append(Player(name))

    def findPlayer(self, name: str):
        foundPlayer = None
        for player in self.players:
            if player.name() == name:
                foundPlayer = player

        if foundPlayer is None:
            self.addPlayer(name)
            return self.findPlayer(name)

        return foundPlayer


    def removePlayer(self, name: str) -> None:
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
                return

    def actOnPlayer(self) -> None:
        if self.active != None:
            self.irc.privmsg(self.irc.config.channel, "coo coo ~ the %s pigeon has made a clean escape" % self.active.type())
            self.active = None
            return
        # if len(self.players) == 0:
        #     return
        # player = random.choice(self.players)
        pigeon = random.choice(self.pigeons)
        action = random.choice(self.actions)
        # player.changePoints(action.actionPoint)
        self.active = pigeon
        self.irc.privmsg(self.irc.config.channel,  action.act(pigeon.type()))

    def start(self):
        # do interval for every 5 seconds
        RepeatedTimer(self._config.interval(), self.actOnPlayer)

    def attemptShoot(self, nick):
        if self.active == None:
            return "There is no pigeon, what are you shooting at? Creepy lol"
        player = self.findPlayer(nick)
        if player is None:
            print("Player not found")
            return "You are not a player in the game"
        print("Player found")
        randomResult = random.random()
        print("Random result: %s, success rate: %s" % (str(randomResult), str(self.active.success() / 100)))
        shot = randomResult < self.active.success() / 100
        if shot:
            player.addPoints(self.active.points())
            self.active = None
            return "You hit the pigeon! You are a murderer!!!"
        else:
            player.removePoints(10)
            return "You missed the pigeon! poor you! :D"

    def scoreBoard(self):
        message = ""
        for player in self.players:
            message += player.name() + " " + str(player.points()) + " "
        return message

            


