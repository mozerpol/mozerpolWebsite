# plik app.py jest glownym plikiem, ktorego uzywamy do wywolania naszej
# aplikacji. export FLASK_APP=app.py.
from app import create_app
import os


app = create_app(os.getenv('FLASK_CONFIG') or 'development')  # FLASK_CONFIG -
# zmienna srodowiskowa. Ogolnie w tej linii tworzymy aplikacje, dzieki temu
# pozniej bedziemy sie do niej odwolywac w sposob app.cos_tam
# Ta aplikacja, ktora tworzymy to w argumencie przyjmuje ustawienia, ktore
# zdefiniowane sa w pliku config.py. Funkcja wytowrcza create_app znajduje
# sie w pliku app/__init__
