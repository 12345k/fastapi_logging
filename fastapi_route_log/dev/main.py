from log_request import LoggingRoute
from fastapi import Body, FastAPI, HTTPException, Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute

from pydantic import BaseModel
from typing import Optional
import dashboard 

app = FastAPI()
app.router.route_class = LoggingRoute
app.include_router(dashboard.router)

class Item(BaseModel):
    name: str
    manufacturerName: str
    rawMaterialName: str
    inventoryId: Optional[int] = None

@app.post("/hello_world")
async def post_test(item:Item,response: Response):  
    return item

@app.get("/hello_world")
async def get_test(response: Response):  
    return "hello world"

@app.get("/health")
async def get_health(response:Response):
    return {"Status":200,"Health":"Good"}

@app.get("/api/health")
async def get_health(response:Response):
    return {"Status":200,"Health":"Good"}