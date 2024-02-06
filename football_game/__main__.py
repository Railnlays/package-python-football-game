from decouple import config
from sqlalchemy.engine import Engine
from sqlmodel import create_engine, SQLModel, Session

from schemas import *


def main():
    postgres_uri: str = config("POSTGRES_URI")
    engine: Engine = create_engine(postgres_uri)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        team = Team(name="Los Vengadores")
        player = Player(
            name="Ernesto", 
            age=26, 
            salary=10000000000,
            team=team
        )
        session.add(player)
        session.commit()


if __name__ == "__main__":
    main()
