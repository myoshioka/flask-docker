from flask import Flask, jsonify
from app.model.user_model import UserModel
app = Flask(__name__)


@app.route('/')
def index():
    user = UserModel()
    all_user = user.get_all()
    return jsonify(all_user)


@app.route('/user/<id>')
def user(id):
    user = UserModel()
    target = user.get(id)
    return jsonify(target)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
