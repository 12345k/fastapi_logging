
<center><h1> Fastapi Route Log </h1></center>
<p align="center">


<a href="https://pypi.org/project/fastapi-route-log/" target="_blank">
<img src="https://img.shields.io/pypi/v/fastapi-route-log?color=%2334D058label=pypi package" alt="Package version">
</a>
<img alt="License" src="https://img.shields.io/github/license/12345k/fastapi_logging"  />
</p>

A FastAPI router for logging every request.

# Installation

```buildoutcfg
$ pip install fastapi_route_log
```
# Dashboard testing

```python
cd fastapi_route_log
uvicorn dev.main:app --reload
```
check the url: http://localhost:8000/fastapi_dashboard

# Code Sample

```python
from fastapi_route_log.log_request import LoggingRoute

app = FastAPI()
app.router.route_class = LoggingRoute
```
# Example/Test

```python
uvicorn example.main:app --reload
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

