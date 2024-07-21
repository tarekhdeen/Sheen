#!/usr/bin/python3

from flask import Flask, request, jsonify, Blueprint, current_app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import app
from models.user import User
from models import storage
import jwt
import datetime
from app import db

user_bp = Blueprint('user', __name__)

# User Registration
@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(email=data['email'], password=hashed_password, first_name=data['first_name'], last_name=data['last_name'])
    storage.new(new_user)
    storage.save()
    return jsonify({'message': 'User created successfully'}), 201

# User Login
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = db.session.query(User).filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login failed'}), 401
    
    token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.now() + datetime.timedelta(hours=1)}, current_app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'message': 'Login successful!', 'token': token}), 200
    

# View Profile
@user_bp.route('/profile', methods=['GET'])
def profile():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing!'}), 401
    
    token = token.split(" ")[1]

    try:
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        user = db.session.query(User).filter_by(id=data['user_id']).first()
        if not user:
            return jsonify({'message': 'User not found!'}), 404
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired!'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Token is invalid!'}), 401
    except Exception as e:
        return jsonify({'message': f'An error occurred: {str(e)}'}), 401

    return jsonify({'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name})

# Edit Profile
@user_bp.route('/profile', methods=['PUT'])
def edit_profile():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing!'}), 401
    
    token = token.split(" ")[1]

    try:
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        user = db.session.query(User).filter_by(id=data['user_id']).first()
        if not user:
            return jsonify({'message': 'User not found!'}), 404
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired!'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Token is invalid!'}), 401
    except Exception as e:
        return jsonify({'message': f'An error occurred: {str(e)}'}), 401
    
    update_data = request.get_json()
    user.first_name = update_data.get('first_name', user.first_name)
    user.last_name = update_data.get('last_name', user.last_name)
    storage.save()

    return jsonify({'message': 'Profile updated successfully'})
