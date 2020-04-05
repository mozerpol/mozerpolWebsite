# W folderze menu zostal stworzony schemat menu naszej stronki
from flask import Blueprint

menu = Blueprint('menu', __name__)

from . import views
