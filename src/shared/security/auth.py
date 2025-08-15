import jwt
from datetime import datetime, timedelta
from typing import Optional
from pydantic import BaseModel

JWT_SECRET = "mi_clave_secreta"
JWT_ALGORITHM = "HS256"
JWT_EXPIRE_HOURS = 24


class Claims(BaseModel):
    user_id: int
    email: str
    exp: Optional[int] = None  


def generate_jwt(user_id: int, email: str) -> str:
    expiration_time = datetime.utcnow() + timedelta(hours=JWT_EXPIRE_HOURS)
    payload = {
        "user_id": user_id,
        "email": email,
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
            exp=payload.get("exp")
        )
    except jwt.ExpiredSignatureError:
        raise Exception("Token expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")
