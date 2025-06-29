from functools import wraps
from flask import request, abort
import os

API_SECRET = os.getenv("API_SECRET")

def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # first authorize the sender
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            abort(401)
        
        # forbidden or not?
        bearer_token = auth_header.split(" ")[-1]
        if bearer_token != API_SECRET:
            abort(403)
        
        return f(*args, **kwargs)
    
    return wrapper
