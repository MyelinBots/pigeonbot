
class Commands:
    def __init__(self, irc, game):
        self.irc = irc
        self.fantasy = "!"
        self.game = game

    def shoot(self, message, command):
        commandName = "shoot"
        if message.command == 'PRIVMSG':
            if command.command == self.fantasy + commandName:
                # lower case the messageFrom
                shootMessage = self.game.attemptShoot(message.messageFrom.lower())
                self.irc.privmsg(self.irc.config.channel, shootMessage)
        return

    def scoreBoard(self, message, command):
        commandName = "score"
        if message.command == 'PRIVMSG':
            if command.command == self.fantasy + commandName:
                self.irc.privmsg(self.irc.config.channel, "Scoreboard: %s" % self.game.scoreBoard())
        return
