"""
    REQUEST FILES
    - You can define files to be uploaded by the client using File.
    - To request files from client, import File and UploadFile from fastapi.
"""


from fastapi import FastAPI, File, UploadFile
from typing import Annotated

app = FastAPI()

@app.post('/files/')
async def create_file(file: Annotated[bytes, File()]):
    return {'file_size': len(file)}

@app.post('/uploadfile/')
async def create_upload_file(file: UploadFile):
    return {
        'file_name': file.filename,
        'content_type': file.content_type,
        'file': file.file
    }