from flask import render_template  # render_template - metoda, ktora pozwala
# wygenerowac szablonu jakiejs strony w html. Dzieki tej metodzie mozna wywolac
# strone. Flask szuka takiej strony w folderze templates.
from . import main

# ponizej jest obsluga kodu bledu 404
@main.app_errorhandler(404)  # procedura bedzie wywolywana tylko w
# przypadku bledow, ktore pochodza z tras zdefiniowanych w projekcie.
def page_not_found(e):  # zeby dzialalo jak nalezy to w argumencie trzeba
    # przekazac 'e'
   return render_template('404.html'), 404

