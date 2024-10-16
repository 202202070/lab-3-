from flask import jsonify,request,abort
TOKEN="mysecrettoken"

def authenicate_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {TOKEN}":
         abort(401,description="unauthorized")