import uuid
from sqlalchemy import select
from modules.pigeon.db.player import Player


class PlayerRepository:
    def __init__(self, db):
        self.db = db

    def get(self, nick) -> Player:
        session = self.db.getSession()
        stmt = select(Player).where(Player.name == nick)
        result = session.execute(stmt).first()
        player = result[0] if result else None
        return player

    def upsert(self, nick, score, count):
        player = self.get(nick)
        session = self.db.getSession()
        if player is None:
            userid = str(uuid.uuid4())
            player = Player(id=userid, name=nick)
            player.score = score
            player.count = count
            session.add(player)
            session.commit()
        else:
            player.score = score
            player.count = count
            session.commit()

        return

    def delete(self, nick):
        session = self.db.getSession()
        # get player by nick
        player = self.get(nick)
        # delete player
        session.delete(player)
        session.commit()

    def getAll(self) -> list[Player]:
        session = self.db.getSession()
        # sort by highest score
        stmt = select(Player).order_by(Player.score.desc())
        result = session.execute(stmt).scalars().all()
        return result

