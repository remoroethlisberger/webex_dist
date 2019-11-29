from flask import url_for, flash, render_template
from flask_login import current_user, login_user
from werkzeug.utils import redirect

from db import db
from forms.LoginForms import LoginForm, SignupForm
from models.Users import User


def add_login_manager_functions(login_manager):
    login_manager.login_view = 'home.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter_by(id=user_id).first()


def check_login_status(request):
    if current_user.is_authenticated:
        return redirect(url_for('home.show'))

    login_form = LoginForm(request.form)

    if request.method == 'POST':
        if login_form.validate():
            email = request.form.get('email')
            password = request.form.get('password')

            user = User.query.filter_by(email=email).first()
            if user:
                if user.check_password(password=password):
                    login_user(user)
                    next = request.args.get('next')
                    return redirect(next or url_for('home.show'))
        flash('Invalid username and password!')
        return redirect(url_for('home.login'))

    return render_template('admin/login.html', form=LoginForm())


def register_user(request):
    signup_form = SignupForm(request.form)

    if request.method == 'POST':
        if signup_form.validate():

            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')

            existing_user = User.query.filter_by(email=email).first()

            if existing_user is None:
                user = User(name=name, email=email, password=password)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('home.show'))
            flash('A user already exists with that email address')
            return redirect(url_for('home.signup'))

    return render_template('admin/signup.html', form=signup_form)
