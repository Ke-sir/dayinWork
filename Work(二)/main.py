from  sanic  import  Sanic
from  sanic.response  import  json
from  database  import  Database

app  =  Sanic(__name__)

#  MongoDB连接配置
db  =  Database('mongodb://localhost:27017/')

#  用户账号管理功能
@app.route("/users",  methods=["GET"])
async  def  get_users(request):
        users  =  db.get_users()
        return  json(users)

@app.route("/users/<username>",  methods=["GET"])
async  def  get_user(request,  username):
        user  =  db.get_user(username)
        return  json(user)

@app.route("/users",  methods=["POST"])
async  def  create_user(request):
        user_data  =  request.json
        user_id  =  db.create_user(user_data)
        return  json({"message":  "User  created  successfully",  "user_id":  user_id})

@app.route("/users/<username>",  methods=["PUT"])
async  def  update_user(request,  username):
        user_data  =  request.json
        modified_count  =  db.update_user(username,  user_data)
        return  json({"message":  "User  updated  successfully",  "modified_count":  modified_count})

@app.route("/users/<username>",  methods=["DELETE"])
async  def  delete_user(request,  username):
        deleted_count  =  db.delete_user(username)
        return  json({"message":  "User  deleted  successfully",  "deleted_count":  deleted_count})

#  权限管理功能
@app.route("/permissions",  methods=["GET"])
async  def  get_permissions(request):
        permissions  =  db.get_permissions()
        return  json(permissions)

@app.route("/permissions",  methods=["POST"])
async  def  create_permission(request):
        permission_data  =  request.json
        permission_id  =  db.create_permission(permission_data)
        return  json({"message":  "Permission  created  successfully",  "permission_id":  permission_id})

@app.route("/permissions/<permission_id>",  methods=["PUT"])
async  def  update_permission(request,  permission_id):
        permission_data  =  request.json
        modified_count  =  db.update_permission(permission_id,  permission_data)
        return  json({"message":  "Permission  update  successfully",  "modified_count":  modified_count})

@app.route("/permissions/<permission_id>",  methods=["DELETE"])
async  def  delete_permission(request,  permission_id):
        deleted_count  =  db.delete_permission(permission_id)
        return  json({"message":  "Permission  deleted  successfully",  "deleted_count":  deleted_count})

#  部门管理功能
@app.route("/departments",  methods=["POST"])
async  def  create_department(request):
        department_data  =  request.json
        department_id  =  db.create_department(department_data)
        return  json({"message":  "Department  created  successfully",  "department_id":  department_id})

@app.route("/departments/<department_id>",  methods=["PUT"])
async  def  update_department(request,  department_id):
        department_data  =  request.json
        modified_count  =  db.update_department(department_id,  department_data)
        return  json({"message":  "Department  updated  successfully",  "modified_count":  modified_count})

@app.route("/departments/<department_id>",  methods=["DELETE"])
async  def  delete_department(request,  department_id):
        deleted_count  =  db.delete_department(department_id)
        return  json({"message":  "Department  deleted  successfully",  "deleted_count":  deleted_count})

if  __name__  ==  '__main__':
        app.run(host="0.0.0.0",  port=8000)