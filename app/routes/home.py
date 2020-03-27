from flask import Blueprint, render_template, abort, request, redirect, url_for
from flask_login import login_required, logout_user
from jinja2 import TemplateNotFound

from middleware.auth import check_login_status, register_user, login_through_token

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
    if(request.args.get('token')):
        login_through_token(request.args.get('token'))
        return redirect('/admin')
    else:
        return check_login_status(request)


@home.route("/logout")
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('home.login'))


@home.route('/signup', methods=['GET', 'POST'])
def signup():
    return register_user(request)
