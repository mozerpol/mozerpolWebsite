# W tym pliku znajduja sie modele bazy danych, relacje miedzy nimi itp. Model
# jest zwyczajna klasa pythona z atrybutami odpowiadajacymi kolumnom przypisanej
# mu tabeli baz danych.
from . import db  # import bazy danych z pliku app/__init__.py


# Ponizsza klasa to definicja modelu Pytanie. 
class Pytanie(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # pierwszy argument
    # konstruktora db.Column jest typ kolumny bazy danych. Jezeli primary_key
    # ma wartosc True, to kolumna jest kluczem glownym tabeli.
    pytanie = db.Column(db.String(255), unique=True)
    odpok = db.Column(db.String(100))
    odpowiedzi = db.relationship(
        'Odpowiedz',
        backref=db.backref('pytanie'),
        cascade="all, delete, delete-orphan"
        )  # atrybut odpowiedzi dodany do tego modelu reprezentuje obiektowy
        # widok relacji widziany z jednej strony. Pierwszy argument funkcji
        # db.relationship wskazuje, ktory z modeli znajduje sie po drugiej
        # stronie relacji. Argument backref w wywolaniu tej funkcji definiuje
        # odwrotny kierunek relacji.


class Odpowiedz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pnr = db.Column(db.Integer, db.ForeignKey('pytanie.id'))  # kolumna
    # pnr dodana do modelu Odpowiedz jest definiowana jako klucz obcy, ktory
    # ustanawia relacje. Argument pytanie.id okresla, ze podana kolumna powinna
    # przechowywac jedynie wartosci z kolumny id w tabeli Pytanie.
    odpowiedz = db.Column(db.String(100))
