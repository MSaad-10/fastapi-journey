"""
    CORS (CORSS-ORIGIN RESOURCE SHARING)
    - CORS refers to the situations when a frontend running in a browser has JavaScript code that communicates with a backend.
    - And the backend is in a different "origin" than the frontend.
    - CORS allows you to control which frontend origins are permitted by the browser to make cross-origin requests to your FastAPI backend.
"""


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
async def main():
    return {'message': 'Hello World'}