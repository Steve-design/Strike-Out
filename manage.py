rom app import create_app,db
from app.models import User,Pitch,Comment
from  flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server

app = create_app('development')