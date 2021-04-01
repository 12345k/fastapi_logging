from fastapi_route_log.log_request import LoggingRoute
from fastapi import Body, FastAPI, HTTPException, Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute

from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.router.route_class = LoggingRoute


class Item(BaseModel):
    name: str
    manufacturerName: str
    rawMaterialName: str
    inventoryId: Optional[int] = None

@app.post("/hello_world")
async def get_test(item:Item,response: Response):

    
  
    return item