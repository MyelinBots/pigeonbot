import threading
import random

from .actions import Action
from .player import Player
from pyircsdk import Module

from .timer import RepeatedTimer


class PigeonModule(Module):
    def __init__(self, irc):
        super().__init__(irc, "", "")
        self.game: Game = Game(irc)
        self.game.start()
        # listen to every message, check for joins to add players

    def handleCommand(self, message, command):
        # add players on join
        if message.command == "JOIN" and message.messageFrom != self.irc.config.nick:
            print("adding player", message.messageFrom)
            self.game.addPlayer(message.messageFrom)

        # 353 is the response to the NAMES command
        if message.command == "353":
            print("adding players from NAMES")
            print(message)
            # get after 4th param
            params = message.params[4:]
            for name in params:
                # remove @ and +
                name = name.lstrip("@")
                name = name.lstrip("+")

                print("adding player", name)
                self.game.addPlayer(name)

        if message.command == "PRIVMSG":
            if command.command == self.fantasy + self.command:
                self.irc.privmsg(message.messageTo, "The pigeon module is not implemented yet.")
                return

    def handleError(self, message, command, error):
        if message.command == "PRIVMSG":
            if command.command == self.fantasy + self.command:
                self.irc.privmsg(message.messageTo, "The pigeon module is not implemented yet.")
                return


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

