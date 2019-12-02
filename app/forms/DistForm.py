from wtforms import Form, TextAreaField, SelectField, SubmitField, SelectMultipleField, MultipleFileField, FileField
from wtforms.validators import DataRequired

from services.bot import all_spaces


class DistForm(Form):
    """Distribution Form."""
    message = TextAreaField('Message',
                          validators=[DataRequired(message='Please enter a message')])
    rooms = SelectMultipleField('Rooms', choices=all_spaces(),
                        validators=[DataRequired(message='Please select a room')])
    files = MultipleFileField('File')
    submit = SubmitField('Send')
