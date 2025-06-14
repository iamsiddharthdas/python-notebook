from fastapi import UploadFile,FastAPI,Response,Request
import os
import uuid
app=FastAPI()

UPLOAD_FOLDER="static"
os.makedirs(UPLOAD_FOLDER,exist_ok=True)
async def upload_file(request:Request,response:Response,file:UploadFile):
    if not file.filename:
        response.status_code=400
        return {"error":"No file name","success":False}
    
    unique_filename=f"{uuid.uuid4()}{file.filename}"
    file_path=os.path.join(UPLOAD_FOLDER,unique_filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
        
    url=f"{request.url.scheme}://{request.url.netloc}/static/{unique_filename}"
    
    return {"filename": url, "saved_to": file_path}
