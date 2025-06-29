from flask import Blueprint, request, jsonify
from models.user import User

user_routes = Blueprint("user_routes", __name__)

@user_route.route("/api/user", methods = ["POST"])
def create_user():
    data = request.get_json() # sends payload
    user = User.from_dict(data)
    return jsonify(user.to_dict()), 201

