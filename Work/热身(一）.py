from sanic import Sanic, response
from motor.motor_asyncio import AsyncIOMotorClient

app = Sanic(__name__)

# 连接MongoDB
mongo_client = AsyncIOMotorClient('mongodb://localhost:27017')
db = mongo_client['bookstore']


@app.route('/books', methods=['GET'])
async def get_books(request):
    collection = db['books']
    books = await collection.find().to_list(length=None)  # 获取所有书籍
    return response.json(books)


@app.route('/book/<id>', methods=['GET'])
async def get_book(request, id):
    collection = db['books']
    book = await collection.find_one({'_id': id})  # 根据ID获取书籍
    if book:
        return response.json(book)
    else:
        return response.json({'error': '没找到书'}, status=404)


@app.route('/book/create', methods=['POST'])
async def create_book(request):
    book_data = request.json
    collection = db['books']
    result = await collection.insert_one(book_data)  # 创建书籍
    return response.json({'id': str(result.inserted_id)})


@app.route('/book/update', methods=['PUT'])
async def update_book(request):
    book_data = request.json
    collection = db['books']
    result = await collection.update_one({'_id': book_data['_id']}, {'$set': book_data})  # 更新书籍
    if result.modified_count == 1:
        return response.json({'message': '图书更新成功'})
    else:
        return response.json({'error': '没找到书'}, status=404)


@app.route('/book/<id>', methods=['DELETE'])
async def delete_book(request, id):
    collection = db['books']
    result = await collection.delete_one({'_id': id})  # 删除书籍
    if result.deleted_count == 1:
        return response.json({'message': '图书删除成功'})
    else:
        return response.json({'error': '没找到书'}, status=404)


# 运行Sanic应用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)