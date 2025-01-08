from datetime import datetime, timedelta, timezone
import jwt
import os
from dotenv import load_dotenv
from functools import wraps
from flask import request, jsonify

# Load environment variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in the environment!")

ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

# Helper function to decode token
def decode_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired!', 'error': 'Unauthorized'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token!', 'error': 'Unauthorized'}), 401

# Encode JWT token
def encode_token(user_id, roles):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(days=1),
        'iat': datetime.now(timezone.utc),
        'sub': user_id,
        'roles': roles
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Decorator: Token required
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', None)
        if token:
            token = token.split(" ")[1] if " " in token else None
        if not token:
            return jsonify({'message': 'Token is missing!', 'error': 'Unauthorized'}), 401

        payload = decode_token(token)
        if isinstance(payload, tuple):
            return payload

        return f(*args, **kwargs)
    return decorated

# Decorator: Role required
def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization', None)
            if token:
                token = token.split(" ")[1] if " " in token else None
            if not token:
                return jsonify({'message': 'Token is missing!', 'error': 'Unauthorized'}), 401

            payload = decode_token(token)
            if isinstance(payload, tuple):
                return payload

            roles = payload.get('roles', [])
            if role not in roles:
                return jsonify({'message': 'Unauthorized access!', 'error': 'Unauthorized'}), 401

            return f(*args, **kwargs)
        return decorated
    return decorator
