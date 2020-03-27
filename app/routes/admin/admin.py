from flask import Blueprint, request
from flask_login import login_required, current_user

from services.admin import show_dist_form

admin = Blueprint('admin', __name__,
                  template_folder='templates', static_folder='/static')


@admin.route('/', methods=['POST', 'GET'])
@login_required
def show():
    return show_dist_form(request)
