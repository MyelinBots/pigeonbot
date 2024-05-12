from pyircsdk import IRCSDKConfig, IRCSDK, Module
import os

from modules.pigeon.main import PigeonModule

host = os.getenv('HOST', 'irc.rizon.net')
port = os.getenv('PORT', '6697')
# convert port string to int
port = int(port)
ssl = os.getenv('SSL', 'False')
nick = os.getenv('NICK', 'PigeonBot')
channel = os.getenv('CHANNEL', '#toolbot')
user = os.getenv('USER', 'PigeonBot')
realname = os.getenv('REALNAME', 'PigeonBot')
nickservFormat = os.getenv('NICKSERV_FORMAT', 'nickserv :identify %s')
nickservPassword = os.getenv('NICKSERV_PASSWORD', None)
passw = os.getenv('PASS', None)
nodataTimeout = os.getenv('NODATA_TIMEOUT', 120)

irc = IRCSDK(IRCSDKConfig(
    host=host,
    port=port,
    nick=nick,
    # string false to boolean
    ssl=ssl == 'True',
    channel=channel,
    user=user,
    realname=realname,
    nickservFormat=nickservFormat,
    nickservPassword=nickservPassword,
    password=passw,
    nodataTimeout=nodataTimeout
))

pigeonModule = PigeonModule(irc)
pigeonModule.startListening()

irc.connect(None)
