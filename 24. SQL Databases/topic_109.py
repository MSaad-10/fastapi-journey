"""
    CREATE MULTIPLE MODELS
    - In SQLModel, any model class that has table=True is a table model.
    - And any model class that doesn't have table=True is a data model.
    - These ones are actually just Pydantic models (with a couple of small extra features). 
    - With SQLModel, we can use inheritance to avoid duplicating all the fields in all the cases.
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

class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=True, index=True)

class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    secret_name: str

class HeroPublic(HeroBase):
    id: int

class HeroCreate(HeroBase):
    secret_name: str

class HeroUpdate(HeroBase):
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None

@app.on_event('startup')
def on_startup():
    create_db_and_tables()

@app.post('/heroes/', tags=['Create Hero'], response_model=HeroPublic)
def create_hero(hero: HeroCreate, session: SessionDep):
    db_hero = Hero.model_validate(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero

@app.get('/heroes/', tags=['Get Heroes'], response_model=list[HeroPublic])
def read_heores(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes

@app.get('/heroes/{hero_id}', tags=['Get Hero'], response_model=HeroPublic)
def read_hero(hero_id: int, session: SessionDep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Hero not found')
    return hero

@app.patch('/heroes/{hero_id}', response_model=HeroPublic, tags=['Update Hero'])
def update_hero(hero_id: int, hero: HeroUpdate, session: SessionDep):
    hero_db = session.get(Hero, hero_id)
    if not hero_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Hero not found')
    hero_data = hero.model_dump(exclude_unset=True)
    hero_db.sqlmodel_update(hero_data)
    session.add(hero_db)
    session.commit()
    session.refresh(hero_db)
    return hero_db

@app.delete('/heroes/{hero_id}', tags=['Delete Hero'])
def delete_hero(hero_id: int, session: SessionDep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Hero not found')
    session.delete(hero)
    session.commit()
    return {'ok': True}