from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Response
from fastapi.routing import APIRoute
from fastapi import APIRouter
import sqlite3
import json
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from collections import Counter


router = APIRouter()
security = HTTPBasic()






# router.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

count = 0

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "12345")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


def utils(val):
    data = []
    for key in range(len(val)):
        data.append(val[key]["ENDPOINT"])
    new_data  = Counter(data)
    del data
    new_data = dict(new_data)
    data = []
    for key,value in new_data.items():
        temp_json = {}
        temp_json["name"] = key
        temp_json["count"] = value
        data.append(temp_json)
    return data

@router.get("/fastapi_dashboard")
async def read_item(request: Request,credentials: HTTPBasicCredentials = Depends(get_current_username)):
    conn = sqlite3.connect('./database/test.db')
    conn.row_factory = sqlite3.Row 
    cursor = conn.execute("SELECT * FROM REQUEST").fetchall()
    len_cursor = len(cursor)
    temp_data = [dict(ix) for ix in cursor]
    data = json.dumps( [dict(ix) for ix in cursor] ) #CREATE JSON
    end_cursor = conn.execute("SELECT DISTINCT ENDPOINT FROM REQUEST").fetchall()
    end_json_temp = [dict(ix) for ix in end_cursor]
    print(end_json_temp)
    # end_json = json.dumps([dict(ix) for ix in end_cursor])

    api_counts = utils(temp_data)
    end_json = utils(end_json_temp)
    # end_json
    conn.close()
    return templates.TemplateResponse("index.html", {"request": request,
                                                         "data":data,
                                                         "count":len_cursor,
                                                         "API":end_json,
                                                         "API_Frequency":api_counts})



@router.get("/fastapi_dashboard/api_frequency")
async def api_frequency():#request: Request,credentials: HTTPBasicCredentials = Depends(get_current_username)):
    conn = sqlite3.connect('./database/test.db')
    conn.row_factory = sqlite3.Row 
    cursor = conn.execute("SELECT * FROM REQUEST").fetchall()
    len_cursor = len(cursor)
    temp_data = [dict(ix) for ix in cursor]
    data = json.dumps( [dict(ix) for ix in cursor] ) #CREATE JSON
    end_cursor = conn.execute("SELECT DISTINCT ENDPOINT FROM REQUEST").fetchall()
    end_json_temp = [dict(ix) for ix in end_cursor]
    print(end_json_temp)
    # end_json = json.dumps([dict(ix) for ix in end_cursor])

    api_counts = utils(temp_data)
    end_json = utils(end_json_temp)
    # end_json
    conn.close()
    return api_counts

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
