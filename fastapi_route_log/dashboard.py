from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Response
from fastapi.routing import APIRoute
from fastapi import APIRouter
import sqlite3
import json


router = APIRouter()


router.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

count = 0

@router.get("/fastapi_dashboard")
async def read_item(request: Request):
    conn = sqlite3.connect('./data/test.db')
    conn.row_factory = sqlite3.Row 
    cursor = conn.execute("SELECT * FROM REQUEST").fetchall()
    len_cursor = len(cursor)
    
    data= json.dumps( [dict(ix) for ix in cursor] ) #CREATE JSON

    
    conn.close()
    return templates.TemplateResponse("dashboard.html", {"request": request,
                                                         "data":data,
                                                         "count":len_cursor})

    # data = """

    #             <!DOCTYPE html>
    #             <html lang="en">
    #             <head>
    #                 <meta charset="UTF-8">
    #                 <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #                 <title>Dashboard</title>
    #             </head>
    #             <body>
    #                 <h1> hello world to dashboard </h1>
    #             </body>
    #             </html>

    # """
    # return Response(content=data, media_type="text/html")
