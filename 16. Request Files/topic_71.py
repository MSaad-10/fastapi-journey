"""
    UploadFile  WITH ADDITIONAL Metadata
    - You can also use File() with UploadFile, for example, to set additional metadata.
"""


from fastapi import FastAPI, File, UploadFile
from typing import Annotated

app = FastAPI()

@app.post('/files/')
async def create_file(
    file: Annotated[bytes, File(description='A file read as bytes')]
):
    return {'file_size': len(file)}

@app.post('/uploadfile')
async def create_upload_file(
    file: Annotated[UploadFile, File(description='A file read as UploadFile')]
):
    return {'file_name': file.filename, 'file_size': file.size}