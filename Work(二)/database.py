from  pymongo  import  MongoClient
from  bson.objectid  import  ObjectId

class  Database:
        def  __init__(self,  db_url):
                self.client  =  MongoClient(db_url)
                self.db  =  self.client['UserManagement']
                self.users_collection  =  self.db['users']
                self.permissions_collection  =  self.db['permissions']
                self.departments_collection  =  self.db['departments']

        def  get_users(self):
                return  list(self.users_collection.find())

        def  get_user(self,  username):
                return  self.users_collection.find_one({"username":  username})

        def  create_user(self,  user_data):
                result  =  self.users_collection.insert_one(user_data)
                return  str(result.inserted_id)

        def  update_user(self,  username,  user_data):
                result  =  self.users_collection.update_one({"username":  username},  {"$set":  user_data})
                return  result.modified_count

        def  delete_user(self,  username):
                result  =  self.users_collection.delete_one({"username":  username})
                return  result.deleted_count

        def  get_permissions(self):
                return  list(self.permissions_collection.find())

        def  create_permission(self,  permission_data):
                result  =  self.permissions_collection.insert_one(permission_data)
                return  str(result.inserted_id)

        def  update_permission(self,  permission_id,  permission_data):
                result  =  self.permissions_collection.update_one({"_id":  ObjectId(permission_id)},  {"$set":  permission_data})
                return  result.modified_count

        def  delete_permission(self,  permission_id):
                result  =  self.permissions_collection.delete_one({"_id":  ObjectId(permission_id)})
                return  result.deleted_count

        def  create_department(self,  department_data):
                result  =  self.departments_collection.insert_one(department_data)
                return  str(result.inserted_id)

        def  update_department(self,  department_id,  department_data):
                result  =  self.departments_collection.update_one({"_id":  ObjectId(department_id)},  {"$set":  department_data})
                return  result.modified_count

        def  delete_department(self,  department_id):
                result  =  self.departments_collection.delete_one({"_id":  ObjectId(department_id)})
                return  result.deleted_count