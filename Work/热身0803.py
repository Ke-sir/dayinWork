from sanic import Sanic
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from pydantic import BaseModel
import bson


class Response(BaseModel):
    message: str


class Result(BaseModel):
    json_data: Optional[dict] = None


class Database:
    def __init__(self):
        self.mongo_client = AsyncIOMotorClient('mongodb://localhost:27017')
        self.db = self.mongo_client['bookstore']
        self.collection = self.db['books']

    async def create(self, book_data):
        result = await self.collection.insert_one(book_data)
        return Response(message=str(result.inserted_id))

    async def read_all(self):
        books = await self.collection.find().to_list(length=None)
        return Result(json_data=books)

    async def read_by_id(self, book_id):
        book = await self.collection.find_one({'_id': bson.ObjectId(book_id)})
        return Result(json_data=book)

    async def update(self, book_data):
        book_id = book_data['_id']
        result = await self.collection.update_one({'_id':  bson.ObjectId(book_id)}, {'$set': book_data})
        if result.modified_count == 1:
            return Response(message='图书更新成功')
        else:
            return Response(message='没找到书')

    async def delete(self, book_id):
        result = await self.collection.delete_one({'_id': bson.ObjectId(book_id)})
        if result.deleted_count == 1:
            return Response(message='图书删除成功')
        else:
            return Response(message='没找到书')


app = Sanic(__name__)
db = Database()


@app.route('/books', methods=['GET'])
async def get_books(request):
    result = await db.read_all()
    return result.json_data


@app.route('/book/<id>', methods=['GET'])
async def get_book(request, id):
    result = await db.read_by_id(id)
    if result.json_data:
        return result.json_data
    else:
        return Response(message='没找到书').json()


@app.route('/book/create', methods=['POST'])
async def create_book(request):
    book_data = request.json
    result = await db.create(book_data)
    return result.json()


@app.route('/book/update', methods=['PUT'])
async def update_book(request):
    book_data = request.json
    result = await db.update(book_data)
    return result.json()


@app.route('/book/<id>', methods=['DELETE'])
async def delete_book(request, id):
    result = await db.delete(id)
    return result.json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
