from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select, and_, or_, col


class Hero(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


engine = create_engine("sqlite:///db.sqlite", echo=False)

''' this will create the database and table'''


def create_db_and_tables():
    print("creating database and table")
    SQLModel.metadata.create_all(engine)


def create_hero():
    print("insert a new record")
    # hero = Hero(name="Itachi Uchiha", secret_name="The clan killer")
    hero1 = Hero(name="Madara Uchiha", secret_name="The ghost of the Uchiha")
    hero2 = Hero(name="Sasuke Uchiha", secret_name="The last Uchiha")
    hero3 = Hero(name="Kakashi Hatake", secret_name="The copt ninja")
    with Session(engine) as session:
        session.add(hero1)
        session.add(hero2)
        session.add(hero3)
        session.commit()
        session.close()


def read_all_heroes():
    print("read all records")
    with Session(engine) as session:
        results = session.exec(select(Hero))
        for hero in results:
            print(hero)
        session.close()


def where_clause():
    print("where clause examples")
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == 'Itachi Uchiha')
        results = session.exec(statement)
        for hero in results:
            print(hero)
        session.close()


def where_and_clause():
    print("where and clause")
    with Session(engine) as session:
        statement = select(Hero).where(and_(Hero.name == 'Kakashi Hatake', Hero.user_id == 4))
        results = session.exec(statement)
        for hero in results:
            print(hero)
        session.close()


def where_or_clause():
    print("where or clause")
    with Session(engine) as session:
        statement = select(Hero).where(or_(Hero.name == 'Kakashi Hatake', Hero.user_id == 3))
        results = session.exec(statement)
        for hero in results:
            print(hero)
        session.close()


def where_like_clause():
    print("where like clause")
    with Session(engine) as session:
        statement = select(Hero).where(col(Hero.name).ilike("%uchiha"))
        results = session.exec(statement)
        for hero in results:
            print(hero)
        session.close()


def main():
    create_db_and_tables()
    # create_hero()
    read_all_heroes()
    where_clause()
    where_and_clause()
    where_or_clause()
    where_like_clause()


if __name__ == "__main__":
    main()
