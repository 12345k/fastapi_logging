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
from datetime import datetime

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


def utils(val,value):
    data = []
    for key in range(len(val)):
        data.append(val[key][value])
    new_data  = Counter(data)
    new_data = dict(new_data)
    temp_data = []
    for key,value in new_data.items():
        temp_json = {}
        temp_json["name"] = key
        temp_json["count"] = value
        temp_data.append(temp_json)
    return temp_data,data

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

    api_counts,_ = utils(temp_data,"ENDPOINT")
    end_json,end_list = utils(end_json_temp,"ENDPOINT")
    # end_json
    conn.close()
    return templates.TemplateResponse("index.html", {"request": request,
                                                         "data":data,
                                                         "count":len_cursor,
                                                         "API":end_json,
                                                         "API_Frequency":api_counts,
                                                         "List_OF_ENDPOINT":end_list})



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

    api_counts,data = utils(temp_data,"ENDPOINT")
   
    end_json = utils(end_json_temp,"ENDPOINT")
    # end_json
    conn.close()
    return api_counts



@router.get("/fastapi_dashboard/api_time_count")
async def time_count():#request: Request,credentials: HTTPBasicCredentials = Depends(get_current_username)):
    conn = sqlite3.connect('./database/test.db')
    conn.row_factory = sqlite3.Row 
    end_cursor = conn.execute("SELECT TIME,COUNT(TIME) AS COUNT FROM REQUEST GROUP BY TIME").fetchall()
    for i in end_cursor:
        print(i["TIME"])
    end_json_temp =  [[datetime.strptime(i["TIME"],'%Y-%m-%d %H:%M:%S'),i['COUNT']] for i in end_cursor]
    print(end_json_temp)
    print("*******************")
    # end_json = json.dumps([dict(ix) for ix in end_cursor])

    # api_counts,data = utils(temp_data,"TIME")
   
    # end_json = utils(end_json_temp,"TIME")
    # # end_json
    # conn.close()
    return end_json_temp
    # return Response(content=end_json_temp, media_type="application/json")

