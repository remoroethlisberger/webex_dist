import os

from flask import render_template
from werkzeug.utils import secure_filename
from services.bot import send_message, all_spaces
from forms.DistForm import DistForm
from models.Favorites import Favorites
from db import db


def show_dist_form(request):
    dist_form = DistForm(request.form)
    dist_form.rooms.choices = mark_favorites(all_spaces())
    dist_form.favs = get_all_favorites()

    if request.method == 'POST':
        if dist_form.validate():
            message = request.form.get('message')
            rooms = request.form.getlist('rooms')
            files = request.files.getlist('files')
            filenames = []
            for file in files:
                if file.filename:
                    filename = secure_filename(file.filename)
                    file.save(os.path.join('./static/uploads', filename))
                    filenames.append(os.path.join('./static/uploads', filename))
            messages = send_message(message, filenames, rooms)
            return render_template('admin/message_sent.html', messages=messages)
    return render_template('admin/dist.html', form=dist_form)

def mark_favorites(array_of_choices):
    choices = []
    for choice in array_of_choices:
        if is_favorite(choice[0]):
            choices.append((choice[0], choice[1] + ' &#11088;'))
        else:
            choices.append(choice)

    return choices

def is_favorite(roomid):
    return Favorites.query.filter_by(roomid=roomid).first()


def delete_all_favorites():
    delete_q = Favorites.__table__.delete().where(True)
    db.session.execute(delete_q)
    db.session.commit()
    return

def add_all_favorites(favorites):
    for favorite in favorites:
        fav = Favorites(roomid=favorite)
        db.session.add(fav)
        db.session.commit()
    return

def get_all_favorites():
    favs = Favorites.query.all()
    res = []
    for fav in favs:
        res.append(fav.roomid)
    return res