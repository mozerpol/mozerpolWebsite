# W tym pliku miesci sie funkcja wytworcza, blueprinty itp.
from flask import Flask  # importowanie flaska
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy to framework do
# relacyjnych baz danych, czyli SQL, a nie noSQL.
from config import config  # dzieki temu mozemy uzywac metody from_object


bootstrap = Bootstrap()
db = SQLAlchemy()  # obiekt db tworzony jest jako instancja klasy
# SQLAlchemym ktory reprezentuje beze danych i zapewnia dostep do wszysytkich
# funkcji flask-SQLAlchemy


def create_app(config_name):  # ta funkcja to funkcja wytworcza, ktora jako
    # argument przyjmuje nazwe konfiguracji, ktora znajduje sie w pliku
    # config.py
    app = Flask(__name__)  # to __name__ mowi flaskowi gdzie znajduje sie
    # aplikacja wydaje mi sie, ze jest to taki punkt odniesienia.
    config_name = 'development'  # nie wiem czemu, ale trzeba na sztywno
    # ustawic nazwe configu, bo kurde nie moze zassac z piliku config.py
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)  # wywolanie init_app uzupelnia inicjalizacje [?]
    db.init_app(app)
    
    from .main import main as main_blueprint  # rejestracja schematu. Dzieki
    # temu moge uzywac jakby modulow. W sensie w jakims folderze moge miec
    # np funkcje odpowiedzialne za logowanie.
    app.register_blueprint(main_blueprint)
    
    from .menu import menu as menu_blueprint
    app.register_blueprint(menu_blueprint, url_prefix='/menu')  # argument
    # url_prefix jest wymagany podczas rejestrowania schematu. Jezeli zostanie
    # uzyty to wszystkie trasy zdefiniowane w tym schemacie beda rejestrowane
    # z przypisanym mu przedrostkiem. W tym przypadku bedzie to przedrostek menu
    
    return app
