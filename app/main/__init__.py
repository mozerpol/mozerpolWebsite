# blueprinty pozwalaja nam implementowac pewno modulowosc i definiowac zbior
# operacji, do ktorych bedziemy sie odwolywac w aplikacji.
from flask import Blueprint


main = Blueprint('main', __name__)  # konstruktor, ktory tworzy schemat pobiera
# dwa argumenty: nazwe projektu oraz modul lub pakiet, w ktorym znajduje sie
# schemat.

from . import views, errors  # skladnia "from . import <pewien-modul> jest
# uzywana w pythonie do zapisywania importu wzglednego. Znak kropki reprezentuje
# aktualny pakiet.
