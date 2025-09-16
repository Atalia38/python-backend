from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

# Sample data
posts = [
    {"user_id": 1, "id": 101, "title": "First Post", "status": "published"},
    {"user_id": 1, "id": 102, "title": "Second Post", "status": "draft"},
    {"user_id": 2, "id": 201, "title": "Another Post", "status": "published"},
]

@app.get("/users/{user_id}/posts")
def get_user_posts(user_id: int, status: str | None = Query(None)):
    user_posts = [p for p in posts if p["user_id"] == user_id]
    if status:
        user_posts = [p for p in user_posts if p["status"] == status]
    return {"user_id": user_id, "posts": user_posts}





from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
posts = [
    {"user_id": 1, "id": 101, "title": "First Post", "status": "published"},
    {"user_id": 1, "id": 102, "title": "Second Post", "status": "draft"},
    {"user_id": 2, "id": 201, "title": "Another Post", "status": "published"},
]

@app.route('/users/<int:user_id>/posts')
def get_user_posts(user_id):
    status = request.args.get('status')
    user_posts = [p for p in posts if p["user_id"] == user_id]
    if status:
        user_posts = [p for p in user_posts if p["status"] == status]
    return jsonify({"user_id": user_id, "posts": user_posts})

if __name__ == '__main__':
    app.run(debug=True)
