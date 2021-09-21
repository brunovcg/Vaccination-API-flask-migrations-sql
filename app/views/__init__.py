from flask import Flask

from .vaccine_view import bp

def init_app(app: Flask):
    app.register_blueprint(bp)
