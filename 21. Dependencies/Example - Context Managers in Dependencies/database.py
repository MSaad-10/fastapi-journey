from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# SQLite database
DATABASE_URL = "sqlite:///./student.db"

# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread': False}
)

# Create a session factory
DBSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for our SQLAlchemy models
Base = declarative_base()

# Custom Context Manager
class DatabaseContextManager:
    def __init__(self):
        print('Creating database session...')
        self.db = DBSession()
    def __enter__(self):
        print('Entering context manager...')
        return self.db
    def __exit__(self, exc_type, exc_value, traceback):
        print('Closing database session...')
        self.db.close()

# FastAPI Dependency
async def get_db():
    with DatabaseContextManager() as db:
        yield db