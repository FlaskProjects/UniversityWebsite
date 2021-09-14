from config import app
from flask import render_template, request


class StudentView(object):

    @staticmethod
    @app.route('/student/practice')
    def practice():
        return render_template('student/practice.html')

    @staticmethod
    @app.route('/student/timetable')
    def timetable():
        return render_template('student/timetable.html')

    @staticmethod
    @app.route('/student/union')
    def union():
        return render_template('student/union.html')
