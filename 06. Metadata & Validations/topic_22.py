"""
    EXCLUDE PARAMETERS FROM OpenAPI
    - We can exclude a query parameter from the generated OpenAPI schema and automatic documentation systems.
    - To do this, set the parameter 'include_in_schema' of 'Query' to 'False'.
"""


from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/exclude_param/')
async def read_items(
    hidden_query: Annotated[
            str | None, 
            Query(
                include_in_schema=False
            )
        ] = None            # Optional 
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {'hidden_query': 'Not Found'}