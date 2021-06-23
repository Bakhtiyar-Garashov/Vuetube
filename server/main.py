from fastapi import FastAPI
import uvicorn
from starlette.requests import Request
from pytube import YouTube
import time
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Vuetube", version="0.0.1")

origins = [
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
)


@app.get('/')
async def home(request: Request):
    return {"message": "Yeaahh,it worked"}

@app.get('/find/')
async def index(url: str):
    if url and 'youtube' in url:
        video_stream = YouTube(url)
        videos = video_stream.streams.filter(progressive=True)
        return {
            'info':{
                'title': video_stream.title,
                'author': video_stream.author,
                'thumbnail': video_stream.thumbnail_url,
                'description': video_stream.description,
                'duration': time.strftime('%H:%M:%S',time.gmtime(video_stream.length)),
                'views_count': video_stream.views,
                'published_date': video_stream.publish_date,
                'download_options': [{'url':video.url,'quality':video.resolution} for video in videos]
             }   
        }
    return {
        'info':{
            'error':'Enter a proper url'
        }
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7500)
