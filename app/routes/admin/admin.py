from flask import Blueprint, request

from services.admin import show_dist_form

admin = Blueprint('admin', __name__,
                  template_folder='templates', static_folder='/static')


@admin.route('/', methods=['POST', 'GET'])
def show():
    return show_dist_form(request)
