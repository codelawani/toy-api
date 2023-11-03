# from .views import app_views
from models.user import User
from flask import Flask, jsonify, request
from os import getenv
from models.engine import storage

app = Flask(__name__)


@app.route('/')
def index():
    return 'Home'


@app.route('/api/status')
def status():
    return jsonify({'status': 'ok'})


@app.teardown_appcontext
def close_db(e):
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': "Not found"}), 404


@app.route('/api/users', strict_slashes=False)
def get_users():
    objects = storage.all()
    user_list = []
    for obj in objects:
        user_list.append(obj.to_dict())
    return user_list


@app.route('/api/user/<id>', strict_slashes=False)
def get_user_by_id(id):
    user = storage.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return user.to_dict()


@app.route('/api/users', methods=['POST'], strict_slashes=False)
def create_users():
    if not request.is_json:
        return jsonify({'error': 'Expected Json data'}, 400)
    data = request.get_json()
    new_user = User(**data)
    storage.new(new_user)
    print(new_user)

    return jsonify(new_user.to_dict()), 201


if __name__ == '__main__':
    host = getenv('host') or '0.0.0.0'
    port = getenv('port') or 5000
    app.run(host=host, port=port, debug=True, threaded=True)
