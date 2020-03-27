from flask import Blueprint, abort, request
from jinja2 import TemplateNotFound
from webexteamssdk import Webhook
import secrets
from services.bot import is_authorized, send_login_link, is_me, send_error_message, get_email
from models.Credentials import Credentials

from db import db

api = Blueprint('api', __name__,
                template_folder='templates')


@api.route('/', methods=['POST'])
def show():
    try:
        data = request.json
        webhook_obj = Webhook(data)
        if is_me(webhook_obj):
            return 'OK'
        elif is_authorized(webhook_obj):
            token = secrets.token_hex(15)
            credentials = Credentials(token=token, email=get_email(webhook_obj))
            db.session.add(credentials)
            db.session.commit()
            send_login_link(webhook_obj, token)
        else:
            send_error_message(webhook_obj)
        return 'OK'
    except TemplateNotFound:
        abort(404)
