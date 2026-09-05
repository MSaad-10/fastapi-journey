"""
    SQL DATABASES
    - FastAPI doesn't require you to use a SQL (relational) database.
    - But you can use any database that you want using SQLMOdel.
    - SQLModel is built on top of SQLAlchemy and Pydantic. 
    - It was made by the same author of FastAPI to be the perfect match for FastAPI applications that need to use SQL databases.
    - As SQLModel is based on SQLAlchemy, you can easily use any database supported by SQLAlchemy, like:
        * PostgreSQL
        * MySQL
        * SQLite
        * Oracle
        * Microsoft SQL Server, etc.
"""


from fastapi import FastAPI, Depends, HTTPException, Query, status
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Annotated

sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

connect_args = {'check_same_thread': False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
app = FastAPI(title='Heroes API')

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str

@app.on_event('startup')
def on_startup():
    create_db_and_tables()

@app.post('/heroes/', tags=['Create Hero'])
def create_hero(hero: Hero, session: SessionDep) -> Hero:
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero

@app.get('/heroes/', tags=['Get Heroes'])
def read_heores(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100) -> list[Hero]:
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes

@app.get('/heroes/{hero_id}', tags=['Get Hero'])
def read_hero(hero_id: int, session: SessionDep) -> Hero:
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Hero not found')
    return hero

@app.delete('/heroes/{hero_id}', tags=['Delete Hero'])
def delete_hero(hero_id: int, session: SessionDep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Hero not found')
    session.delete(hero)
    session.commit()
    return {'ok': True}