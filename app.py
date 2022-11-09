from fastapi import FastAPI, Form, HTTPException, Body
from fastapi.responses import HTMLResponse
from urllib3.util import parse_url
import requests
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def untrack_tiktok(url):
    if not url:
        raise HTTPException(status_code=400, detail="URL is required")
    parsed_url = parse_url(url)
    if not "tiktok.com" in parsed_url.host:
        raise HTTPException(status_code=400, detail="Invalid URL")
    r = requests.head(parsed_url.url) 
    u = parse_url(r.headers["Location"])
    return u.scheme + "://" + u.host + u.path
    # TODO: better error handling
    # TODO: better URL parsing (e.g. addig https:// if not present)


@app.post("/tt-untrack-form/") 
async def tt_untrack_form(url: str = Form()):
    return untrack_tiktok(url)
    # TODO: make this return a HTML page with the untracked URL

@app.post("/tt-untrack/")
async def tt_untrack(url: str = Body(embed=True)):
    return untrack_tiktok(url)




@app.get("/", response_class=HTMLResponse) 
async def index(): 
    index = """<!DOCTYPE html>
<html>
<head>
    <title>untrack TikTok links</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, 
    initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
</head>
<body>
    <form action="/tt-untrack-form" method="post"> <label class="form-label" for="url"> Tik Tok share URL</label> <input
            class="form-control" id="url" name="url" type="text"> <br /> <button class="form-control" type="submit">
            submit </button>
</body>
</html> """
    return index
	
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
