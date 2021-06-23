from typing import Optional
from fastapi import FastAPI
import uvicorn
from starlette.requests import Request
from pytube import YouTube
import time

app = FastAPI(title="First project", version="0.0.1")

@app.get('/')
async def home(request: Request):
    return {"message": "Yeaahh,it worked"}

@app.get('/find/')
async def index(url: str):
    yt = YouTube(url)
    if yt:
        videos = yt.streams.filter(progressive=True);
        return {
            "info":{
                'title':yt.title,
                'author':yt.author,
                'thumbnail':yt.thumbnail_url,
                'description':yt.description,
                'duration':time.strftime('%H:%M:%S',time.gmtime(yt.length)),
                'views_count':yt.views,
                'published_date':yt.publish_date,
                'download_options': [{'url':video.url,'quality':video.resolution} for video in videos]
             }   
        }
    return {
        'info':{
            'message':'Video data not found'
        }
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7500)
