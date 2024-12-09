from app import app
from app.controller import UserController
from flask import request
from app.controller import ProductController, CategoryController

@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.store()
@app.route('/users/<id>', methods=['PUT', 'GET', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return UserController.show(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)


@app.route('/products', methods=['POST', 'GET'])
def products():
    if request.method == 'GET':
        return ProductController.index()
    else:
        return ProductController.store()

@app.route('/products/<id>', methods=['GET', 'PUT', 'DELETE'])
def productDetail(id):
    if request.method == 'GET':
        return ProductController.show(id)
    elif request.method == 'PUT':
        return ProductController.update(id)

@app.route('/products/<product_id>/categories/<category_id>', methods=['POST'])
def addCategoryToProduct(product_id, category_id):
    return ProductController.add_category_to_product(product_id, category_id)

@app.route('/categories', methods=['POST', 'GET'])
def categories():
    if request.method == 'GET':
        return CategoryController.index()
    else:
        return CategoryController.store()

@app.route('/categories/<id>', methods=['GET', 'PUT', 'DELETE'])
def categoryDetail(id):
    if request.method == 'GET':
        return CategoryController.show(id)
    elif request.method == 'PUT':
        return CategoryController.update(id)