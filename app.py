import os
from flask import Flask, render_template, request, jsonify
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

from routes.api.users import users_routes
from routes.api.token import token_routes
from routes.api.register import register_routes

app = Flask(__name__)

app.register_blueprint(users_routes)
app.register_blueprint(token_routes)
app.register_blueprint(register_routes)

if __name__ == '__main__':
    app.run(debug=True)
