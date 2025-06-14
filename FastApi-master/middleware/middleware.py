import jwt
from fastapi import FastAPI, Request,Response,status
async def verify(request:Request,response:Response):
    try:
        token = request.headers['token']
        
        payload=jwt.decode(token, 'Lokesh is the Good Boy', algorithms=['HS256'])
        return payload
    except jwt.PyJWTError as e:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"error": "Token is expired","success":False}
    except jwt.InvalidTokenError as e:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"error": "Invalid Token","success":False}
    except Exception as e:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"error": str(e),"success":False}