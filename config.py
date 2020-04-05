# Czasem jest tak, ze aplikacja wymaga kilku ustawien konfiguracyjnych, np.
# mamy ustawienia do testow i ostateczna konfiguracje. W tym pliku beda sie
# miescic ustawienia, ktore bedziemy mogli sobie pozniej wyrbac co chcemy.
import os  # modul os umozliwia zarzadzac plikami, folderami itp. na kompie
basedir = os.path.abspath(os.path.dirname(__file__))  # pomaga nam zlokalizowac
# baze danych


class Config:
    SECRET_KEY = 'bardzosekretnawartosc'  # ustawienie sekretnej wartosci dla
    # rozszerzen flaska (sam flask tego nie wymaga do dzialania)
    SQLALCHEMY_TRACK_MODIFICATIONS=False  # Dokumentacja sugeruje
    # zeby kluczowi SQLALCHEMY_TRACK_MODIFICATIONS przypisac wartosc false, to
    # wtedy zmniejszamy zuzycie pamieci, bo cos tam sie nie zapisuje.
    
    @staticmethod
    def init_app(app):  # ta metoda jako argument przyjmuje instancje aplikacji
    # tez wymagana jest do poprawnego dzialania
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'quiz.db')  # konfiguracja probuje
        # zaimportowac adres URL bazy danych ze zmiennej srodowiskowej, a gdy
        # nie jest on dostepny to jako domyslny adres przyjmuje bazy SQLite
        
config = {  # zestaw zawierajacy mozliwe ustawienia naszej aplikacji
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
