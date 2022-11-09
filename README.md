# ttuntrack

a simple tool to remove the tracking information from a TikTok share URL and return the original URL.

## Demo

[tu.moroku.de](https://tu.moroku.de)

## Usage

- go to Website
- paste TikTok Share URL
- click on submit
- copy the new URL

or use the API:

```bash
curl -X POST -d '{"url": "https://vm.tiktok.com/ABC2D3EFG"' https://tu.moroku.de/tt-untrack
```

will return the untracked URL as the only thing in the response body.

```text
https://www.tiktok.com/@user/video/1234567890123456789
```

Please use the API responsibly. If you want to use it more often, please host a copy of this project yourself.

## Installation

- adjust the docker-compose.yml file to your needs (e.g. remove the traefik labels, add port mapping)
- run `docker-compose up -d`

or:

- run `docker build -t ttuntrack .`
- run `docker run -d -p 80:80 --name ttuntrack ttuntrack`

or:

- run `pip install -r requirements.txt`
- run `python3 app.py`

## License

[MIT](https://choosealicense.com/licenses/mit/)

Copyright (c) 2022 Moritz Schmidt

## Contributing

Just open a pull request or write a issue :)
