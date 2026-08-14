"""
    Path Parameters Containing Paths
    - You can use path parameters to capture values from the URL path.
    - This can be done using ':path' in the parameter definition.
"""


from fastapi import FastAPI
app = FastAPI()

@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {"file_path": file_path}     