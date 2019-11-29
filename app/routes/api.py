from flask import Blueprint, abort
from jinja2 import TemplateNotFound

api = Blueprint('api', __name__,
                template_folder='templates')


@api.route('/')
def show():
    try:
        return 'OK'
    except TemplateNotFound:
        abort(404)
