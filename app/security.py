# File: app/security.py
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
import os

# Ensure SECRET_KEY is set with a fallback for development
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here-change-in-production')
ALGORITHM = os.getenv('ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 30))

# Validate that SECRET_KEY exists
if not SECRET_KEY or SECRET_KEY == 'your-secret-key-here-change-in-production':
    print("Warning: Using default SECRET_KEY. Set SECRET_KEY environment variable for production!")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    # Ensure SECRET_KEY is not None
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY environment variable is not set")
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str):
    """Verify and decode the access token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.JWTError:
        return None