from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

users = [
    {
        "username": "fengfeng",
        "password": "123456",
        "email": "fengfeng@example.com",
        "age": 18,
        "created_at": "2023-01-01T08:00:00Z"
    },
    {
        "username": "admin",
        "password": "admin123",
        "email": "admin@example.com",
        "age": 25,
        "created_at": "2023-02-15T12:30:00Z"
    },
    {
        "username": "testuser",
        "password": "test123",
        "email": "testuser@example.com",
        "age": 30,
        "created_at": "2023-03-20T18:45:00Z"
    }
]

@app.route("/users",methods=["GET"])
async def get_users(request):
    return json(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
