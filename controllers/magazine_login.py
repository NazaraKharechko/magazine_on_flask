from flask import Blueprint, render_template, redirect, url_for, request
from forms.auth import LoginForm, RegisterForm
from flask_login import current_user, login_user, logout_user
from models import User, Goods
from services.user_service import find_user_by_email

magazine_login = Blueprint("magazine_login", __name__)


@magazine_login.route('/', methods=["GET"])
def index():
    if current_user.is_authenticated == 1:
        return redirect(url_for('magazine_login.positions'))
    if current_user.is_authenticated == 0:
        return redirect(url_for('magazine_login.login'))
    render_template('base.html', current_user=current_user)


@magazine_login.route('/all')
def positions():
    all_goods = Goods.query.all()
    return render_template('magazine.html', all_goods=all_goods, current_user=current_user)


@magazine_login.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(email='attacker@gmail.com')
    error = None
    if request.method == 'POST' and login_form.validate():
        data = dict(login_form.data)
        user = find_user_by_email(data['email'])
        if user and user.check_pass(data['password']):
            login_user(user)
            return redirect(url_for('magazine_login.positions'))
        if user and user.check_pass(data['password']) == 0:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error, login_form=login_form)


@magazine_login.route('/buy', methods=['GET', 'POST'])
def buy():
    return render_template('buy.html')


@magazine_login.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for("magazine_login.index"))
