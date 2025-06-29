from flask import Blueprint, request, jsonify, abort
from models.user import User
from db.crud import add_roblox_user
from util.auth import requires_auth

users_routes = Blueprint("users_routes", __name__)


@users_routes.route("/api/users", methods = ["POST"])
@requires_auth
def create_user():
    data = request.get_json() # sends payload
    user = User.from_dict(data)
    add_roblox_user(user)
    return jsonify(user.to_dict()), 201

