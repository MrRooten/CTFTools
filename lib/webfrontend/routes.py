from .forms import LoginForm
from .models import User
from werkzeug.urls import url_parse
from flask_login import login_user,logout_user,current_user,login_required
from flask import render_template, flash, redirect, url_for, Blueprint

auth = Blueprint('auth',__name__)
@auth.route('/')
@auth.route('/index')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template('index.html')

@auth.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect('index')
    return render_template('login.html',form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

