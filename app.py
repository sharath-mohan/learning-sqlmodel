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


# with Session(engine) as session:
#     hero_1 = Hero(name="Mohan", secret_name="Michel", age=27)
#     session.add(hero_1)
#     session.commit()


if __name__ == "__main__":
    create_db_and_tables()
