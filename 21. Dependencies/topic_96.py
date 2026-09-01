"""
    SUB-DEPENDENCIES WITH yield
    - You can have sub-dependencies and "trees" of sub-dependencies of any size and shape, and any or all of them can use yield.
    - FastAPI will make sure that the "exit code" in each dependency with yield is run in the correct order.
        * For example, dependency_c can have a dependency on dependency_b, and dependency_b on dependency_a
"""


from fastapi import Depends, FastAPI
from typing import Annotated

app = FastAPI()

# Dependency A
async def dependency_a():
    print('A: setup')
    dep_a = 'Resource A'
    try:
        yield dep_a 
    finally:
        print('A: cleanup')

# Dependency B ----> depends on ----> Dependency A
async def dependency_b(dep_a: Annotated[str, Depends(dependency_a)]):
    print(f'B: setup (received {dep_a})')
    dep_b = 'Resource B'
    try:
        yield dep_b
    finally:
        print(f'B: cleanup (still has {dep_a})')

# Dependency C ----> depends on ----> Dependency B
async def dependency_c(dep_b: Annotated[str, Depends(dependency_b)]):
    print(f'C: setup (received {dep_b})')
    dep_c = 'Resource C'
    try:
        yield dep_c
    finally:
        print(f'C: cleanup (still has {dep_b})')

# Endpoint ----> depends on ----> Dependency C
@app.get('/test/')
async def test(dep_c: Annotated[str, Depends(dependency_c)]):
    print(f'Endpoint: received ({dep_c})')
    return {
        'message': 'Success',
        'resource': dep_c
    }