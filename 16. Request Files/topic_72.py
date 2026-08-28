"""
    MULTIPLE FILE UPLOADS
    - It's possible to upload several files at the same time.
    - They would be associated to the same "form field" sent using "form data".
    - To use that, declare a list of bytes or UploadFile.
"""


from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from fastapi.responses import HTMLResponse
from openapi_utils import custom_openapi        # For Swagger UI multiple-file picker button render issue

app = FastAPI()
app.openapi = lambda: custom_openapi(app)

@app.post('/files/')
async def create_files(files: Annotated[list[bytes], File()]):
    return {'file_sizes': [len(file) for file in files]}

@app.post('/uploadfiles/')
async def create_upload_files(files: list[UploadFile] = File(...)):
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