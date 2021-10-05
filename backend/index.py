from fastapi import FastAPI
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from starlette.routing import request_response
from starlette.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware # 追加
from fastapi.responses import StreamingResponse
from typing import List
import os

app = FastAPI(
    title='fb_sandobox',
    description='fb_sandobox example',
    version='1.0 beta'
    )

# CORSを回避するために追加（今回の肝）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)
# app.mount("/favicon.ico", StaticFiles("./dist/favicon.ico"), name="favicon")
app.mount("/video_files", StaticFiles(directory="./dist/video_files"), name="video_files")
app.mount("/vue.sandbox/js", StaticFiles(directory="./dist/js"), name="js")
app.mount("/vue.sandbox/img", StaticFiles(directory="./dist/img"), name="img")
app.mount("/vue.sandbox/wavedrom", StaticFiles(directory="./dist/wavedrom"), name="wavedrom")
app.mount("/vue.sandbox/css", StaticFiles(directory="./dist/css"), name="css")
templates = Jinja2Templates(directory="./dist")
jinja_env = templates.env

def index(request: Request):
    """
    WebUI表示
    """
    return templates.TemplateResponse('index.html', {'request': request})

def chunk_generator_from_stream(filepath, chunk_size, start, size):
    bytes_read = 0

    with open(filepath, mode="rb") as file_like:
        file_like.seek(start)

        while bytes_read < size:
            bytes_to_read = min(chunk_size,
                                size - bytes_read)
            yield file_like.read(bytes_to_read)
            bytes_read = bytes_read + bytes_to_read

BYTES_PER_RESPONSE = 100000
from pathlib import Path
def videofile(foldername, filename, req: Request):
    asked = req.headers.get("Range")
    filepath = os.path.join('E:/Documents/GitHub/vue-sandbox/dist', foldername, filename)
    total_size = Path(filepath).stat().st_size
    start_byte_requested = int(asked.split("=")[-1][:-1])
    end_byte_planned = min(start_byte_requested + BYTES_PER_RESPONSE, total_size) - 1
    chunk_generator = chunk_generator_from_stream(
        filepath,
        chunk_size=10000,
        start=start_byte_requested,
        size=BYTES_PER_RESPONSE
    )
    return StreamingResponse(
        chunk_generator,
        media_type="video/mp4",
        headers={
            "Accept-Ranges": "bytes",
            "Content-Range": f"bytes {start_byte_requested}-{end_byte_planned}/{total_size}",
            "Content-Type": "..."
        },
        status_code=206)
