# W tym pliku mieszcza sie wszystkie widoki poza index.html, ktory jest w
# app/main/views.py 
from flask import render_template, request, url_for
from flask import flash  # Dzieki temu mozna wyswietlac komunikaty
from flask import redirect  # dzieki redirect mozna zrobic przekierowanie.
from . import menu
from .. import db  # import bazy danych. Sa dwie kropki, poniewaz zawiera sie
# dwa foldery wczesniej
from ..models import Pytanie, Odpowiedz


@menu.route('/categories', methods=['GET', 'POST'])  # menu - bo znajdujemy sie w tym
# folderze?
def lista():
    # GET, wyświetl pytania
    pytania = Pytanie.query.join(Odpowiedz)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('main.index'))

    return render_template('categories.html', pytania=pytania.all())
    
    
@menu.route('/electronics', methods=['GET', 'POST'])
def quiz():
    # POST, sprawdź odpowiedzi
    if request.method == 'POST':
        wynik = 0  # liczba poprawnych odpowiedzi
        # odczytujemy słownik z odpowiedziami
        for pid, odp in request.form.items():
            # pobieramy z bazy poprawną odpowiedź
            odpok = db.session.query(Pytanie.odpok).filter(
                Pytanie.id == int(pid)).scalar()
            if odp == odpok:  # porównujemy odpowiedzi
                wynik += 1  # zwiększamy wynik
        # przygotowujemy informacje o wyniku
        flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(wynik), 'sukces')
        return redirect(url_for('main.index'))

    # GET, wyświetl pytania
    pytania = Pytanie.query.join(Odpowiedz)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('main.index'))

    return render_template('electronics.html', pytania=pytania.all())
    
    
@menu.route('/programming', methods=['GET', 'POST'])
def dodaj():
    error = []
    # POST, zapisz pytanie
    if request.method == 'POST':
        # sprawdzanie poprawności przesłanych danych
        if len(request.form['pytanie']) == 0:
            error.append(u'Błąd: pytanie nie może być puste!')
        odpowiedzi = list(request.form.getlist('odp[]'))
        for odp in odpowiedzi:
            if len(odp) == 0:
                error.append(u'Odpowiedź nie może być pusta!')
        if len(request.form['odpok']) == 0:
            error.append(u'Brak numeru poprawnej odpowiedzi!')
        elif int(request.form['odpok']) > len(odpowiedzi):
            error.append(u'Błędny numer poprawnej odpowiedzi!')

        if not error:  # jeżeli nie ma błędów dodajemy pytanie
            pytanie = request.form['pytanie'].strip()
            odpok = odpowiedzi[(int(request.form['odpok']) - 1)]
            try:
                if request.form['id']:  # aktualizujemy pytanie
                    p = Pytanie.query.get(request.form['id'])
                    p.pytanie = pytanie.strip()
                    p.odpok = odpok.strip()
                    for i, odp in enumerate(odpowiedzi):
                        p.odpowiedzi[i].odpowiedz = odp.strip()
                    db.session.commit()
                    flash(u'Zmieniono pytanie:', 'sukces')
            except KeyError:  # dodajemy nowe pytanie, brak id pytania!
                p = Pytanie(pytanie=pytanie.strip(), odpok=odpok.strip())
                db.session.add(p)
                db.session.commit()
                for odp in odpowiedzi:
                    o = Odpowiedz(pnr=p.id, odpowiedz=odp.strip())
                    db.session.add(o)
                db.session.commit()
                flash(u'Dodano pytanie:', 'sukces')

            flash("\n" + pytanie + " " + odpok.strip() +
                  " (" + ", ".join(odpowiedzi) + ")", 'kom')
            return redirect(url_for('main.index'))
        else:
            for e in error:
                flash(e, 'blad')

    # GET, wyświetl formularz
    return render_template('programming.html')
    
@menu.route('/usun', methods=['GET', 'POST'])
def usun():
    pytania = Pytanie.query.join(Odpowiedz)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        pid = request.form['id']
        p = Pytanie.query.get(pid)
        db.session.delete(p)
        db.session.commit()
        flash(u'Usunięto pytanie {0}'.format(pid), 'sukces')
    return render_template('usun.html', pytania=pytania.all())


@menu.route('/edytuj', methods=['GET', 'POST'])
def edytuj():
    pytania = Pytanie.query.join(Odpowiedz)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        pid = request.form['id']
        pytanie = Pytanie.query.get(pid)
        return render_template('programming.html', pytanie=pytanie)

    return render_template('edytuj.html', pytania=pytania.all())
    

@menu.route('/electronicsPost')
def electronicsPost():
    return render_template('electronicsPost.html')
