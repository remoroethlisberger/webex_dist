import os

from flask import render_template
from werkzeug.utils import secure_filename
from services.bot import send_message, all_spaces
from forms.DistForm import DistForm


def show_dist_form(request):
    dist_form = DistForm(request.form)
    dist_form.rooms.choices = all_spaces()

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
            send_message(message, filenames, rooms)
            return render_template('admin/message_sent.html')
    return render_template('admin/dist.html', form=dist_form)
