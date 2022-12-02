from flask import Flask

class frontend:

    def create_app():
        from .views import views

        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'asdsdgtrbfgbrdfsdf'

        app.register_blueprint(views, url_prefix='/')

        return app
