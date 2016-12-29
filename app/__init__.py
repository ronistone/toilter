from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_login import LoginManager
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app,db)

lm = LoginManager()
lm.init_app(app)

mail = Mail(app)

#msg = Message("Teste", sender=app.config['MAIL_USERNAME'], recipients=['ronistone.junior@gmail.com'])
#msg.body =  "Você tem um livro pra devolver"
#mail.send(msg)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.models import tables
from app.controllers import default

#verifica = tables.Envio()
#verifica.start()
