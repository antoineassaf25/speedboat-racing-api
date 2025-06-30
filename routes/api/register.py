from flask import Blueprint, request, abort, jsonify
from models.api_user import APIUser
from db.crud import register_user
from datetime import datetime, timedelta
import jwt
import os

register_routes = Blueprint("register_routes", __name__)
JWT_SECRET = os.getenv("JWT_SECRET")
REGISTRATION_SECRET = os.getenv("REGISTRATION_SECRET")

@register_routes.route('/api/register', methods = ["POST"])
def register():
    
    data = request.get_json()

    # check if the auth matches the create user database secret

    auth_header = request.headers.get("Authorization")

    if auth_header != f"Bearer {REGISTRATION_SECRET}":
        abort(403, description="Invalid signup key")

    # make user object and add to register user, make them an admin
    api_user = APIUser.create_with_plain_password(data['username'], data['password'], 'ADMIN')
    result = register_user(api_user)

    if result:
        return "User Registered, now call token", 200
    else:
        abort(409, description="User already exists")
    

    



    