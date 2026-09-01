"""
    USING CONTEXT MANAGERS IN DEPENDENCIES WITH yield
    - In Python, you can create Context Managers by creating a class with two methods: __enter__() and __exit__().
    - You can also use them inside of FastAPI dependencies with yield by using with or async with statements inside of the dependency function.
    - This file contains the prototype of the implementation.
    - The complete working example is present in "Example - Context Managers in Dependencies" folder.
"""


class MySuperContextManager:
    def __init__(self):
        self.db = DBSession()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()

async def get_db():
    with MySuperContextManager() as db:
        yield db