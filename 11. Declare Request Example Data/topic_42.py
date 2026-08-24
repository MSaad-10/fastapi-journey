"""
    EXTRA JSON SCHEME DATA IN PYDANTIC MODELS
    - You can declare examples for a Pydantic model that will be added to the generated JSON Schema.
    - That extra info will be added as-is to the output JSON Schema for that model, and it will be used in the API docs.
"""


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    'name': 'Fan',
                    'description': 'A very nice item',
                    'price': 35.4,
                    'tax': 2.3,
                }
            ]
        }
    }

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, 'item': item}