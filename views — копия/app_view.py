from config import app
from flask import render_template, request


class AppView(object):

    @staticmethod
    @app.route('/applicants/bachelor')
    def bachelor():
        return render_template('applicants/bachelor.html')

    @staticmethod
    @app.route('/applicants/master')
    def master():
        return render_template('applicants/master.html')

    @staticmethod
    @app.route('/applicants/scientist')
    def scientist():
        return render_template('applicants/scientist.html')
