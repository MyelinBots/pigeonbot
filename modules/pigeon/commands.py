
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
    
    def scorePigeon(self, message, command):
        commandName = "pigeons"
        if message.command == 'PRIVMSG':
            if command.command == self.fantasy + commandName:
                self.irc.privmsg(self.irc.config.channel, "Pigeons shot: %s" % self.game.Pigeonsshot(message.messageFrom.lower()))
        return
    
    def bef(self, message, command):
        commandName = "bef"
        if message.command == 'PRIVMSG':
            if command.command == self.fantasy + commandName:
                self.irc.privmsg(self.irc.config.channel, "You cannot be friend with *rat of the sky*")
        return

