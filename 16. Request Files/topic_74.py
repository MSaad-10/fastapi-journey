"""
    REQUEST FILE AND FORMS
    - You can define files and form fields at the same time using File and Form.
"""


from fastapi import FastAPI, File, Form, UploadFile
from typing import Annotated

app = FastAPI()

@app.post('/files/')
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()]
):
    return {
        'file_size': len(file),
        'token': token,
        'fileb_content_type': fileb.content_type
    }