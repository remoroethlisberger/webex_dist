from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import app
import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)