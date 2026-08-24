"""
    USING THE openapi_examples PARAMETER
    - You can declare the OpenAPI-specific examples in FastAPI with the parameter openapi_examples for:
        * Path(), Query(), Header(), Cookie(), Body(), Form(), File()
    - The keys of the dict identify each example, and each value is another dict.
    - Each specific example dict in the examples can contain:
        * summary
        * description
        * value
"""


from typing import Annotated
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None 

@app.put('/items/{item_id}')
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            openapi_examples={
                'normal': {
                    'summary': 'An example with normal data',
                    'description': 'A **normal** item works correctly',
                    'value': {
                        'name': 'Marker',
                        'description': 'A tool used to write',
                        'price': 35.2,
                        'tax': 1.2,
                    },
                },
                'converted': {
                    'summary': 'An example with converted data',
                    'description': 'FastAPI can convert price `strings` to actual `numbers` automatically.',
                    'value': {
                        'name': 'PS5',
                        'price': '1234',
                    },
                },
                'invalid': {
                    'summary': 'An example with invalid data',
                    'description': 'Invalid data is rejected with an error',
                    'value': {
                        'name': 'Notebook',
                        'price': 'thirty four point six',
                    },
                },
            },
        ),
    ],
):
    return {'item_id': item_id, 'item': item}
