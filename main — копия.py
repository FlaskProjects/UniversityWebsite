from config import app
from views.app_view import AppView
from views.home_view import HomeView
from views.partner_view import PartnerView
from views.student_view import StudentView



if __name__ == '__main__':
    av = AppView()
    hv = HomeView()
    pv = PartnerView()
    sv = StudentView()
    app.run(debug=True)
