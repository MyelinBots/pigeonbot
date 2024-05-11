from .actions import Action
from .player import Player
from .timer import RepeatedTimer
from .pigeon import Pigeon, pigeons
import random
class Game:
    def __init__(self, irc):
        self.irc = irc
        self.players: [Player] = []
        self.actions: [Action] = [
            Action("stole", ["tv", "wallet", "food"], "a %s pigeon %s your %s", 10),
            Action("pooped", ["car", "table", "head"], "a %s pigeon %s on your %s", 10),
            Action("landed", ["balcony", "head", "car", "house"], "a %s pigeon has %s on your %s", 10),
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
        RepeatedTimer(10, self.actOnPlayer)

    def attemptShoot(self, nick):
        if self.active == None:
            return "There is no pigeon, what are you shooting at?"
        player = self.findPlayer(nick)
        if player is None:
            print("Player not found")
            return "You are not a player in the game"
        print("Player found")
        shot = random.random() < self.active.success() / 100
        if shot:
            player.addPoints(self.active.points())
            self.active = None
            return "You hit the pigeon!"
        else:
            player.removePoints(10)
            return "You missed the pigeon!"

    def scoreBoard(self):
        message = ""
        for player in self.players:
            message += player.name() + " " + str(player.points()) + " "
        return message

            


