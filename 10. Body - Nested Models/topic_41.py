"""
    BODIES OF PURE lists
    - If the top level value of the JSON body you expect is a JSON array (a Python list).
    - You can declare the type in the parameter of the function, the same as in Pydantic models.
"""


from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

@app.post('/images/multiple/')
async def create_multiple_images(images: list[Image]):
    return images



"""
    BODIES OF ARBITRARY dicts
    - You can also declare a body as a dict with keys of some type and values of some other type.
    - For the given example, you would accept any dict as long as it has int keys with float values.    
"""


from fastapi import FastAPI

app = FastAPI()

@app.post('/index-weights/')
async def create_index_weights(weights: dict[int, float]):
    print(weights)
    print(type(next(iter(weights.keys()))))
    return weights