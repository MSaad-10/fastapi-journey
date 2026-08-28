"""
    OPTIONAL FILE UPLOAD
    - You can make a file optional.
    - It can be done by using standard type annotations and setting a default value of None.
"""


from fastapi import FastAPI, File, UploadFile
from typing import Annotated

app = FastAPI()

@app.post('/files/')
async def create_file(file: Annotated[bytes | None, File()] = None):
    if not file:
        return {'message': 'No file sent'}
    return {'file_size': len(file)}

@app.post('uploadfile')
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {'message': 'No file sent'}
    return {'file_name': file.filename}