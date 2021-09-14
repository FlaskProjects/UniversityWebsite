from config import app
from flask import render_template, request


class HomeView(object):

    @staticmethod
    @app.route('/home/about')
    def about():
        return render_template('home/about.html')

    @staticmethod
    @app.route('/home/index')
    def index():
        return render_template('home/index.html')

    @staticmethod
    @app.route('/home/institutions')
    def institutions():
        return render_template('home/institutions.html')

    @staticmethod
    @app.route('/home/science')
    def science():
        return render_template('home/science.html')
