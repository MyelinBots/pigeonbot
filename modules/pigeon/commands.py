
class Commands:
    def __init__(self, irc, game):
        self.irc = irc
        self.fantasy = "!"
        self.game = game

    def shoot(self, message, command):
        commandName = "shoot"
        if message.command == 'PRIVMSG':
            if command.command == self.fantasy + commandName:
                self.irc.privmsg(message.messageTo, "Bang! You're dead!")
        return
