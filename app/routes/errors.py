from flask import render_template


def add_custom_error_pages(app):
    @app.errorhandler(401)
    def not_authorized(e):
        return render_template('errors/401.html')
