from fastapi import FastAPI, Form from fastapi.responses import 
HTMLResponse from urllib3.util import parse_url import requests import 
uvicorn app = FastAPI() @app.post("/tt-untrack/") async def 
untrack_tiktok(url: str = Form()):
	parsed_url = parse_url(url) r = requests.head(parsed_url.url) u 
	= parse_url(r.headers["Location"]) return u.scheme + "://" + 
	u.host + u.path
	
@app.get("/", response_class=HTMLResponse) async def index(): index = 
	"""
 <!DOCTYPE html> <html> <head> <title>untrack TikTok links</title> <meta 
    charset="utf-8"> <meta name="viewport" content="width=device-width, 
    initial-scale=1"> <link 
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" 
    rel="stylesheet" 
    integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" 
    crossorigin="anonymous">
</head> <body> <form action="/tt-untrack" method="post"> <label 
class="form-label" for="url"> Tik Tok share URL</label> <input 
class="form-control" id="url" name="url" type="text"> <br/> <button 
class="form-control" type="submit"> submit </button> </body> </html> """
	return index
	
#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8080)
