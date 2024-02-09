import csv
from decouple import config
from sqlmodel import create_engine, SQLModel, Session
from sqlmodel import Session

from schemas import *


def main():
    postgres_uri: str = config("POSTGRES_URI")
    engine = create_engine(postgres_uri)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        with open("test_player.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(**row)
                session.add(player)
            session.commit()
            print("Data inserted successfully!")


if __name__ == "__main__":
    main()
