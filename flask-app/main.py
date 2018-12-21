from flask import Flask, jsonify, render_template, request, redirect, url_for, abort
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from flask_bootstrap import Bootstrap
import requests
import json
from db.orm.user import User
from app.forms.login_form import LoginForm


app = Flask(__name__)
app.secret_key = 'secretstring'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
bootstrap = Bootstrap(app)


@app.route('/')
@login_required
def index():
    #api_url = 'http://host.docker.internal:5000'
    api_url = 'http://api:5000'
    response = requests.get(api_url)
    user_data = json.loads(response.text)
    return render_template('index.html', user_data=user_data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        next = request.args.get('next')
        return redirect(next or url_for('index'))

    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        form.name.data = ''
        form.password.data = ''
        user = User.name(name)
        print(user)
        if user is not None and user.password == password:
            login_user(user)
            next = request.args.get('next')
            return redirect(next or url_for('index'))
        else:
            return render_template('login.html', form=form, error=True)

    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('login')


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
