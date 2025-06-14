from fastapi import FastAPI, Request,Response
from pymongo import *
from bson import ObjectId
from middleware.middleware import verify
from model.Notes import Notes
from pydantic import ValidationError
from bson import ObjectId
client=MongoClient('mongodb://localhost:27017/fastapi')
db=client["fastapi"]


async def insert_notes(request:Request,response:Response):
    try:
        mynotes=db["notes"]
        myuser=db["users"]
        token=await verify(request,response)
        token=dict(token)
        
        exist=myuser.find_one({"_id":ObjectId(token["id"])})
        if not exist:
            response.status_code=400
            return {"error":"User not found","success":False}

        if not token["id"] or not ObjectId.is_valid(token["id"]):
            response.status_code=400
            return {"error":"Invalid User","success":False}

        data=await request.json()
        data=dict(data)
        note = Notes(**data)
        note=dict(note)
        
        result=mynotes.insert_one({"studentId":ObjectId(token["id"]),**note})
        
        if not result.inserted_id:
            response.status_code=400
            return {"error":"Notes not inserted","success":False}
        
        
        return {"message": "Notes Inserted Successfully","success":True}
    except ValidationError as e:
        response.status_code=400
        return {"error":e.errors(),"success":False}
    except Exception as e:
        print(" jai mata di")
        response.status_code=500
        return {"error":str(e),"success":False}
    
    
    
async def get_notes(request: Request, response: Response):
    try:
        token = await verify(request, response)
        token = dict(token)
        myuser = db["users"]
        mynotes = db["notes"]
        
        exist = myuser.find_one({"_id": ObjectId(token["id"])})
        if not exist:
            response.status_code = 400
            return {"error": "User not found", "success": False}
        
        result = mynotes.find({"studentId": ObjectId(token["id"])})
        
        # Convert ObjectId to string for every note
        notes_list = []
        for note in result:
            note["_id"] = str(note["_id"])  # Convert ObjectId to string
            note["studentId"] = str(note["studentId"])  # Convert studentId (ObjectId) to string
            notes_list.append(note)

        return {"data": notes_list, "success": True}
    except ValidationError as e:
        response.status_code = 400
        return {"error": e.errors(), "success": False}
    except Exception as e:
        response.status_code = 500
        return {"error": str(e), "success": False}


async def delete_notes(request: Request, response: Response):
    try:
        token=await verify(request,response)
        token=dict(token)
        myuser=db["users"]
        mynotes=db["notes"]
        
        exist=myuser.find_one({"_id":ObjectId(token["id"])})
        if not exist:
            response.status_code=400
            return {"error":"User not found","success":False}
        
        data=await request.json()
        data=dict(data)
        if not data["_id"] or not ObjectId.is_valid(data["_id"]):
            response.status_code=400
            return {"error":"Invalid Note","success":False}
        
        result=mynotes.delete_one({"_id":ObjectId(data["_id"])})
        print(result)
        if not result.deleted_count:
            response.status_code=400
            return {"message":"Notes not deleted","success":False}
        
        return {"message": "Notes Deleted Successfully","success":True}
        
        
        
    except ValidationError as e:
        response.status_code = 400
        return {"error": e.errors(), "success": False}
    except Exception as e:
        
        response.status_code = 500
        return {"error": str(e), "success": False}
    
    
    
async def update_notes(request: Request, response: Response):
    try:
        token=await verify(request,response)
        token=dict(token)
        myuser=db["users"]
        mynotes=db["notes"]
        
        exist=myuser.find_one({"_id":ObjectId(token["id"])})
        if not exist:
            response.status_code=400
            return {"error":"User not found","success":False}
        
        data=await request.json()
        data=dict(data)
        note=Notes(**data)
        if not data["_id"] or not ObjectId.is_valid(data["_id"]):
            response.status_code=400
            return {"error":"Invalid Note","success":False}
        
        
        result=mynotes.update_one({"_id":ObjectId(data["_id"])},{"$set":{"title":note.title,"notes":note.notes}})
        if not result.modified_count:
            response.status_code=400
            return {"message":"Notes not updated","success":False}
        
        return {"message": "Notes Updated Successfully","success":True}
        
        
        
    except ValidationError as e:
        response.status_code = 400
        return {"error": e.errors(), "success": False}
    except Exception as e:
        print(e)
        response.status_code = 500
        return {"error": str(e), "success": False}