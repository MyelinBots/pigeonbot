from pyircsdk import IRCSDKConfig, IRCSDK, Module
import os

from modules.pigeon.main import PigeonModule

host = os.getenv('HOST', 'irc.rizon.net')
port = os.getenv('PORT', '6667')
# convert port string to int
port = int(port)
nick = os.getenv('NICK', 'PigeonBot')
channel = os.getenv('CHANNEL', '#toolbot')
realname = os.getenv('REALNAME', 'PigeonBot')

irc = IRCSDK(IRCSDKConfig(
    host,
    port,
    nick,
    channel,
    realname
))

pigeonModule = PigeonModule(irc)
pigeonModule.startListening()

irc.connect(None)
