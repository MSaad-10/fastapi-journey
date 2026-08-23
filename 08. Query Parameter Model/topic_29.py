"""
    QUERY PARAMETER MODEL
    - If you have a group of query parameters that are related, you can create a Pydantic model to declare them.
    - This would allow you to re-use the model in multiple places.
    - Also, it will allow you to declare validations and metadata for all the parameters at once.
"""


from fastapi import FastAPI, Query
from typing import Annotated, Literal
from pydantic import BaseModel, Field

app = FastAPI()

class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@app.get('/items/')
async def read_items(
    filter_query: Annotated[FilterParams, Query()]
):
    return filter_query