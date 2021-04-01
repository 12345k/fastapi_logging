# fastapi_route_log

A FastAPI router for logging every request

# Installation

```buildoutcfg
$ pip install fastapi_route_log
```


# Code Sample

```python
from fastapi_route_log.log_request import LoggingRoute

app = FastAPI()
app.router.route_class = LoggingRoute
```


# Output

```json
{
    "type": "request",
    "uuid": "29da7a45-e673-4b15-94bf-3e51737de6b3",
    "env": null,
    "region": null,
    "name": null,
    "method": "POST",
    "useragent": {
        "family": "insomnia",
        "major": 2020,
        "minor": 5,
        "patch": "2020.5.0",
        "device": {
            "family": "Other",
            "brand": null,
            "model": null,
            "major": "0",
            "minor": "0",
            "patch": "0"
        },
        "os": {
            "family": "Other",
            "major": 0,
            "minor": 0,
            "patch": ""
        }
    },
    "url": "/hello_world",
    "query": {
        "get": [
            "hello"
        ]
    },
    "body": {
        "rawMaterialName": "TC-407",
        "manufacturerName": "Tokuriki Honten Co., Ltd.",
        "name": "karthicks"
    },
    "length": null,
    "ts": "2021-04-01 18:48:19"
}
{
    "type": "metrics",
    "uuid": "29da7a45-e673-4b15-94bf-3e51737de6b3",
    "env": null,
    "region": null,
    "name": null,
    "method": "POST",
    "status_code": 200,
    "url": "/hello_world",
    "query": {
        "get": [
            "hello"
        ]
    },
    "length": "113",
    "latency": "0.26",
    "ts": "2021-04-01 18:48:19"
}
INFO:     127.0.0.1:45872 - "POST /hello_world?get=hello HTTP/1.1" 200 OK

```

# License

MIT