from flask import Blueprint, request
from flask_login import login_required, current_user

from services.admin import show_dist_form, delete_all_favorites, add_all_favorites

admin = Blueprint('admin', __name__,
                  template_folder='templates', static_folder='/static')


@admin.route('/', methods=['POST', 'GET'])
@login_required
def show():
    return show_dist_form(request)


@admin.route('/favs', methods=['POST'])
def set_favorites():
    content = request.get_json()
    if content['favorites']:
        favorites = content['favorites']
        delete_all_favorites()
        add_all_favorites(favorites)
            
    return 'OK'