"""
    MULTIPLE FILE UPLOADS WITH ADDITIONAL Metadata
    - The same way as before, you can use File() to set additional parameters, even for UploadFile.
"""


from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from fastapi.responses import HTMLResponse
from openapi_utils import custom_openapi

app = FastAPI()
app.openapi = lambda: custom_openapi(app)

@app.post('/files')
async def create_files(
    files: Annotated[list[bytes], File(description='Multiple files as bytes')],
):
    return {'file_sizes': [len(file) for file in files]}

@app.post('/uploadfiles')
async def create_upload_files(
    files: Annotated[list[UploadFile], File(description='Multiple files as UploadFile')],
):
    return {'file_names': [file.filename for file in files]}

@app.get('/')
async def main():
    content = """
        <body>
        <form action="/files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        </body>
"""
    return HTMLResponse(content=content)