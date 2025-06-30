from flask import Blueprint, request, abort, jsonify
from models.api_user import APIUser
from db.crud import check_api_user_admin
from datetime import datetime, timedelta
import jwt
import os

token_routes = Blueprint("token_routes", __name__)
JWT_SECRET = os.getenv("JWT_SECRET")

@token_routes.route('/api/token', methods = ["POST"])
def get_token():
    
    data = request.get_json()
    # First create the user
    api_user = APIUser.create_with_plain_password(data['username'], data['password'], 'ADMIN')

    # Now, I need to check if this user exists in the api_users database
    result = check_api_user_admin(api_user, data['password'])

    if result == False:
        abort(403, description="Invalid credentials")

    # valid user, create temporary JWT token

    encoded_jwt = jwt.encode(
        {
            "sub": api_user.username,
            "role": api_user.role,
            "exp":  datetime.utcnow() + timedelta(hours=1)
        },
        JWT_SECRET,
        algorithm="HS256"
    )
    return jsonify({"token": encoded_jwt}), 200
    

    



    