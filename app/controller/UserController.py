from app.model.user import Users
from app import response
from flask import request, jsonify
from app import db
def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.bad_request(message="An error occurred while fetching users.")
def store():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        
        user = Users(name=name, email=email)
        user.setPassword(password)
        
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "Successfully created data!"}), 200

    except Exception as e:
        print(e)
        return jsonify({"message": "An error occurred while creating data!"}), 500
def transform(users):
    array = []
    for i in users:
        array.append({
            'id': i.id,
            'name': i.name,
            'email': i.email
        })
    return array
def update(id):
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        user = Users.query.filter_by(id=id).first()

        if user:
            user.email = email
            user.name = name
            user.setPassword(password)

            db.session.commit()

            return response.ok('', 'Successfully updated data!')
        else:
            return response.error('User not found', 404)
    
    except Exception as e:
        print(e)
        return response.error('An error occurred while updating data', 500)

def singleTransform(users):
    data = {
        'id': users.id,
        'name': users.name,
        'email': users.email
    }
    return data

def show(id):
    try:
        users = Users.query.filter_by(id=id).first()
        
        if not users:
            return response.badRequest([], "User not found.")
        
        data = singleTransform(users)
        return response.ok(data, "User retrieved successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return response.badRequest([], "An error occurred while retrieving the user.")
