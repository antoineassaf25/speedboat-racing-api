import os
from flask import Flask, render_template, request, jsonify
from supabase import create_client, Client

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/race_result_test', methods=['POST'])
def race_result():
    data = request.get_json()
    print(data)
    return jsonify({"status": "received"}), 200

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/sup')
def yo():
    return "What upppp"

if __name__ == '__main__':
    app.run(debug=True)