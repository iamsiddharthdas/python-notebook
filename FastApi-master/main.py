from fastapi import FastAPI, Request,Response,UploadFile
from controller.user import signup,login
from controller.notes import insert_notes,get_notes,delete_notes,update_notes
from controller.fileupload import upload_file
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import uvicorn

import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/signup")
async def user(request:Request,response:Response):
    return await signup(request,response)

@app.post("/login")
async def user(request:Request,response:Response):
    return await login(request,response)

@app.post("/insert-notes")
async def user(request:Request,response:Response):
    return await insert_notes(request,response)

@app.post("/get-notes")
async def user(request:Request,response:Response):
    return await get_notes(request,response)

@app.delete("/delete-notes")
async def user(request:Request,response:Response):
    return await delete_notes(request,response)

@app.put("/update-notes")
async def user(request:Request,response:Response):
    return await update_notes(request,response)

@app.post("/upload-file")
async def user(request:Request,response:Response,file:UploadFile):
    return await upload_file(request,response,file)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
