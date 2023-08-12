from sanic import Sanic
from sanic.response import json
from pymongo import MongoClient

app = Sanic(__name__)

# MongoDB连接配置
client = MongoClient('mongodb://localhost:27017/')
db = client['UserManagement']
users_collection = db['users']
permissions_collection = db['permissions']
departments_collection = db['departments']

# 用户账号管理功能
@app.route("/users", methods=["GET"])
async def get_users(request):
    users = []
    for user in users_collection.find():
        users.append(user)
    return json(users)

@app.route("/users/<username>", methods=["GET"])
async def get_user(request, username):
    user = users_collection.find_one({"username": username})
    return json(user)

@app.route("/users", methods=["POST"])
async def create_user(request):
    user_data = request.json
    result = users_collection.insert_one(user_data)
    return json({"message": "User created successfully", "user_id": str(result.inserted_id)})

@app.route("/users/<username>", methods=["PUT"])
async def update_user(request, username):
    user_data = request.json
    result = users_collection.update_one({"username": username}, {"$set": user_data})
    return json({"message": "User updated successfully", "modified_count": result.modified_count})

@app.route("/users/<username>", methods=["DELETE"])
async def delete_user(request, username):
    result = users_collection.delete_one({"username": username})
    return json({"message": "User deleted successfully", "deleted_count": result.deleted_count})

# 权限管理功能
@app.route("/permissions", methods=["GET"])
async def get_permissions(request):
    permissions = []
    for permission in permissions_collection.find():
        permissions.append(permission)
    return json(permissions)

@app.route("/permissions", methods=["POST"])
async def create_permission(request):
    permission_data = request.json
    result = permissions_collection.insert_one(permission_data)
    return json({"message": "Permission created successfully", "permission_id": str(result.inserted_id)})

@app.route("/permissions/<permission_id>", methods=["PUT"])
async def update_permission(request, permission_id):
    permission_data = request.json
    result = permissions_collection.update_one({"_id": ObjectId(permission_id)}, {"$set": permission_data})
    return json({"message": "Permission updated successfully", "modified_count": result.modified_count})

@app.route("/permissions/<permission_id>", methods=["DELETE"])
async def delete_permission(request, permission_id):
    result = permissions_collection.delete_one({"_id": ObjectId(permission_id)})
    return json({"message": "Permission deleted successfully", "deleted_count": result.deleted_count})

# 部门管理功能
@app.route("/departments", methods=["POST"])
async def create_department(request):
    department_data = request.json
    result = departments_collection.insert_one(department_data)
    return json({"message": "Department created successfully", "department_id": str(result.inserted_id)})

@app.route("/departments/<department_id>", methods=["PUT"])
async def update_department(request, department_id):
    department_data = request.json
    result = departments_collection.update_one({"_id": ObjectId(department_id)}, {"$set": department_data})
    return json({"message": "Department updated successfully", "modified_count": result.modified_count})

@app.route("/departments/<department_id>", methods=["DELETE"])
async def delete_department(request, department_id):
    result = departments_collection.delete_one({"_id": ObjectId(department_id)})
    return json({"message": "Department deleted successfully", "deleted_count": result.deleted_count})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
