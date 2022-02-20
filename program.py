from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
  db = SQLAlchemy()
  db.init_app(app)

  with app.app_context():
    from approutes import routes
    app.register_blueprint(routes)

    db.create_all()

    return app
