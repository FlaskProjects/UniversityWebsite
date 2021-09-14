from config import app
from flask import render_template, request


class PartnerView(object):

    @staticmethod
    @app.route('/partners/letter')
    def letter():
        return render_template('partners/letter.html')
