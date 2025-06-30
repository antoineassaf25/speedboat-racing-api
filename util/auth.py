from functools import wraps
from flask import request, abort
import os
import jwt

JWT_SECRET = os.getenv("JWT_SECRET")

def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        # first authorize the sender with JWT token
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            abort(401, description="Missing or invalid Authorization header")
        
        # authenticate token
        try: 
            bearer_token = jwt.decode(auth_header.split(" ")[-1], JWT_SECRET, algorithms=["HS256"])

            if bearer_token["role"].lower() != "admin":
                abort(403, description="Forbidden: admin access required")
        except jwt.ExpiredSignatureError:
            abort(401, description="Token expired")
        except jwt.InvalidTokenError:
            abort(403, description="Invalid token")
        
        return f(*args, **kwargs)
    
    return wrapper
