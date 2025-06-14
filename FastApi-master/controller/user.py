from fastapi import FastAPI, Request,Response,status
from pydantic import ValidationError
from model.User import User
import bcrypt
import datetime
import jwt
from pymongo import *
client=MongoClient('mongodb://localhost:27017/fastapi')

db=client["fastapi"]

async def signup(request: Request,response:Response):
    try:
        data = await request.json()
        data=User( **dict(data))
        if data.password!=data.cpassword:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"error": "Password and Confirm Password should be same","success":False}
        myuser=db["users"]
        hashed = bcrypt.hashpw(data.password.encode("utf-8"), bcrypt.gensalt())

        exist=myuser.find_one({"email":data.email})
        if exist:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"error": "Email already exist","success":False}
        exist=myuser.find_one({"username":data.username})
        if exist:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"error": "Username already exist","success":False}
        exist=myuser.find_one({"pno":data.pno})
        if exist:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"error": "Phone number already exist","success":False}
        
        result=myuser.insert_one({"username":data.username,"email":data.email,"pno":data.pno,"password":hashed,"created_at":datetime.datetime.now()})
        
        return {"message": "Account Successfully Created","success":True}
    except ValidationError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": e.errors(),"success":False}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e),"success":False}
    
    
async def login(request: Request,response:Response):
    try:
        data=await request.json()
        data=User(**dict(data))
        myuser=db["users"]
        exist=myuser.find_one({"email":data.email})
        if not exist:
            response.status_code=status.HTTP_400_BAD_REQUEST
            return {"error":"Email not found","success":False}
        if not bcrypt.checkpw(data.password.encode("utf-8"),exist["password"]):
            response.status_code=status.HTTP_400_BAD_REQUEST
            return {"error":"Password is incorrect","success":False}
        
        if not bcrypt.checkpw(data.password.encode("utf-8"),exist["password"]):
            response.status_code=status.HTTP_400_BAD_REQUEST
            return {"error":"Password is incorrect","success":False}
        
        payload={"id":str(exist["_id"])}
        encoded = jwt.encode(payload, "Lokesh is the Good Boy", algorithm="HS256")
        
        return {"message": "Login Successfully","success":True,"token":encoded}
    except ValidationError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": e.errors(),"success":False}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e),"success":False}
