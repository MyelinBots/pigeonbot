from pyircsdk import Module
from .commands import Commands
from .game import Game


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

        # for each Commands call function
        commands = Commands(self.irc, self.game)
        for attr_name in dir(commands):
            # Get the attribute
            attr = getattr(commands, attr_name)
            # Check if the attribute is a method and call it
            if callable(attr) and not attr_name.startswith('__'):
                attr(message, command)

        if message.command == "PRIVMSG":
            if command.command == self.fantasy + self.command:
                self.irc.privmsg(message.messageTo, "The pigeon module is not implemented yet.")
                return

    def handleError(self, message, command, error):
        if message.command == "PRIVMSG":
            if command.command == self.fantasy + self.command:
                self.irc.privmsg(message.messageTo, "The pigeon module is not implemented yet.")
                return


