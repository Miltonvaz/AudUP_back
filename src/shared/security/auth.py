import jwt
from datetime import datetime, timedelta
from typing import Optional
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("SECRET_KEY")
JWT_ALGORITHM = os.getenv("ALGORITHM")
JWT_EXPIRE_HOURS = int(os.getenv("ACCESS_TOKEN_EXPIRE_HOURS"))  


class Claims(BaseModel):
    user_id: int
    email: str
    role: str
    exp: Optional[int] = None  


def generate_jwt(user_id: int, email: str, role : str) -> str:
    expiration_time = datetime.utcnow() + timedelta(hours=JWT_EXPIRE_HOURS)
    payload = {
        "user_id": user_id,
        "email": email,
        "role": role, 
        "exp": int(expiration_time.timestamp()) 
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token


def validate_jwt(token: str) -> Claims:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return Claims(
            user_id=payload["user_id"],
            email=payload["email"],
            role=payload["role"], 
            exp=payload.get("exp")
        )
    except jwt.ExpiredSignatureError:
        raise Exception("Token expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")
