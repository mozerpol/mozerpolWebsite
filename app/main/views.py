# W tym pliku znajduje sie glowny widok aplikacji, czyli index.html
from flask import render_template  # render_template - metoda, ktora pozwala
# wygenerowac szablonu jakiejs strony w html. Dzieki tej metodzie mozna wywolac
# strone. Flask szuka takiej strony w folderze templates.
from . import main


@main.route('/')  # main - chyba dlatego, bo sie znadujemy w folderze main
def index():
    return render_template('index.html')
    
