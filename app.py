from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine


class Hero(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


engine = create_engine("sqlite:///db.sqlite", echo=True)

''' this will create the database and table'''


def create_db_and_tables():
    print("creating database and table")
    SQLModel.metadata.create_all(engine)


def create_hero():
    print("insert a new record")
    hero = Hero(name="Itachi Uchiha", secret_name="The clan killer")
    with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.close()


def main():
    create_db_and_tables()
    create_hero()


if __name__ == "__main__":
    main()
