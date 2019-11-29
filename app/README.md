# Main application
This simple flask application is structured as follows:

- **Models**: The main data models used with SQLAlchemy
- **Routes**: All the routes registered through Flask Blueprints
- **Services**: The main services and business logic of this application
- **Templates**: A template folder used for the views (using Jinja 2)
- **Static**: Additional static folder with images, stylesheets and JavaScript code.

To build the application use the command `docker build .`

## Creating the database - using flask-migration
Run `python manage.py db init`, `python manage.py db migrate` and `python manage.py db upgrade` in order to create the database.