import time
from starlette.requests import Request
from typing import Callable
from fastapi import HTTPException, Request, Response
import time
import os
import uuid
import json
from user_agents import parse
from urllib.parse import parse_qs
from datetime import datetime
from fastapi.routing import APIRoute

class LoggingRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                uuid_str = str(uuid.uuid4())
                header = dict(request.headers)
                if "uuid" in header.keys():
                    uuid_str = header["uuid"]

                user_agent = parse(request.headers["user-agent"])
                
                browser=user_agent.browser.version
                if len(browser) >=2:
                    browser_major,browser_minor = browser[0],browser[1]
                else:
                    browser_major,browser_minor =0,0

                
                user_os=user_agent.os.version
                if len(user_os) >=2:
                    os_major,os_minor = user_os[0],user_os[1]
                else:
                    os_major,os_minor =0,0

                # Request json
                body = await request.body()
                if len(body)!=0:
                    body=json.loads(body)
                else:
                    body=""
                request_json = {
                    "type":"request",
                    "uuid":uuid_str,
                    "env": os.environ.get("ENV"),
                    "region": os.environ.get("REGION"),
                    "name": os.environ.get("NAME"),
                    "method": request.method,
                    "useragent":
                    {
                        "family": user_agent.browser.family,
                        "major":  browser_major,
                        "minor":  browser_minor,
                        "patch":  user_agent.browser.version_string,
                            
                        "device": {
                                "family": user_agent.device.family,
                                "brand": user_agent.device.brand,
                                "model": user_agent.device.model,
                                "major": "0",
                                "minor": "0",
                                "patch": "0"
                            },
                        "os": {
                                "family": user_agent.os.family,
                                "major": os_major,
                                "minor": os_minor,
                                "patch": user_agent.os.version_string 
                            },
                    
                    },
                    "url": request.url.path,
                    "query": parse_qs(str(request.query_params)),
                    "body":body,
                    "length": request.get("content-length"),
                    'ts': f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'   

                }
                
                print(json.dumps(request_json,indent=4))
                
                start_time = time.time()
                response = await original_route_handler(request)
                process_time = (time.time() - start_time) * 1000
                formatted_process_time = '{0:.2f}'.format(process_time)

                metrics_json = {
                    "type": "metrics",
                    "uuid": uuid_str,
                    "env": os.environ.get("ENV"),
                    "region": os.environ.get("REGION"),
                    "name": os.environ.get("NAME"),              
                    "method": request.method,
                    "status_code": response.status_code,
                    "url": request.url.path,
                    "query": parse_qs(str(request.query_params)),
                    "length": response.headers["content-length"],
                    "latency": formatted_process_time,
                    "ts": f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'   

                }
                
                
                print(json.dumps(metrics_json,indent=4))
                return response

            except Exception as exc:

                body = await request.body()

                detail = {"errors": str(exc), "body": body.decode("utf-8")}
                print(detail)

                raise HTTPException(status_code=422, detail=detail)

        return custom_route_handler


