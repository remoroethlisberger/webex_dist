from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash
from jinja2 import TemplateNotFound

from forms.LoginForms import SignupForm, LoginForm
from models.Users import User
from db import db

home = Blueprint('home', __name__,
                 template_folder='templates', static_folder='/static')



@home.route('/')
@login_required
def show():
    try:
        return render_template('/index.html')
    except TemplateNotFound:
        abort(404)


@home.route('/login', methods=['POST', 'GET'])
def login():
    """User login page."""
    # Bypass Login screen if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('home.show'))
    login_form = LoginForm(request.form)
    # POST: Create user and redirect them to the app
    if request.method == 'POST':
        if login_form.validate():
            # Get Form Fields
            email = request.form.get('email')
            password = request.form.get('password')
            # Validate Login Attempt
            user = User.query.filter_by(email=email).first()
            if user:
                if user.check_password(password=password):
                    login_user(user)
                    next = request.args.get('next')
                    return redirect(next or url_for('home.show'))
        flash('Invalid username/password combination')
        return redirect(url_for('home.login'))
    # GET: Serve Log-in page
    return render_template('admin/login.html',
                           form=LoginForm(),
                           title='Log in | Flask-Login Tutorial.',
                           template='login-page',
                           body="Log in with your User account.")


@home.route("/logout")
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('home.login'))


@home.route('/signup', methods=['GET', 'POST'])
def signup():
    """User sign-up page."""
    signup_form = SignupForm(request.form)
    # POST: Sign user in
    if request.method == 'POST':
        if signup_form.validate():
            # Get Form Fields
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            website = request.form.get('website')
            existing_user = User.query.filter_by(email=email).first()
            if existing_user is None:
                user = User(name=name, email=email, password=password)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('home.show'))
            flash('A user already exists with that email address.')
            return redirect(url_for('home.signup'))
    # GET: Serve Sign-up page
    return render_template('admin/signup.html',
                           title='Create an Account | Flask-Login Tutorial.',
                           form=signup_form,
                           template='signup-page',
                           body="Sign up for a user account.")
