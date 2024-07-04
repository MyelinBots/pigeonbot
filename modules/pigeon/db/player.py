from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Player(Base):
    __tablename__ = 'players'

    # automate uuid generation
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    score: Mapped[int] = mapped_column(Integer)
    count: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f'<Player(name={self.name}, score={self.score})>'
