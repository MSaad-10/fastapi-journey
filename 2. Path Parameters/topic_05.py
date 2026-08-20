"""
    PREDEFINED VALUES
    - This FastAPI application demonstrates the use of predefined values using Python's Enum class.
    - We can define a set of predefined values for a path parameter.
    - FastAPI will validate the input against these predefined values and return an error if the input does not match any of them.
"""


from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class ModelName(str, Enum):     # Predefined Values: Enum class defines a set of predefined values for the path parameter
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}