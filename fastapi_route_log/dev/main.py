from log_request import LoggingRoute
from fastapi import Body, FastAPI, HTTPException, Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import dashboard

app = FastAPI()
app.router.route_class = LoggingRoute
app.include_router(dashboard.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    manufacturerName: str
    rawMaterialName: str
    inventoryId: Optional[int] = None

@app.post("/hello_world")
async def post_test(item:Item,response: Response):  
    return item

@app.post("/hello_prasanna")
async def ret_pras():
    return {"Name":"Prasanna Kumar"}

@app.get("/hello_world")
async def get_test(response: Response):  
    return "hello world"