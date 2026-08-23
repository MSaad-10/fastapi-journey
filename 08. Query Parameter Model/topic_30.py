"""
    FORBID EXTRA QUERY PARAMETERS
    - In some special use cases, you might want to restrict the query parameters that you want to receive.
    - You can use Pydantic's 'model configuration' to 'forbid' any 'extra' fields.
"""


from fastapi import FastAPI, Query, Path
from typing import Annotated, Literal
from pydantic import BaseModel, Field

app = FastAPI()

class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
