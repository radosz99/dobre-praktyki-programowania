from package2 import main
from package1 import api_handler
from package1 import api_others
import sys
import time

entries = []
bibtexes = []
api_key = {API_KEY}

MENU = '''\t1: Wyszukaj zasoby po ID autora.
        2: Wyszukaj zasoby po ID autora i stronie
        3: Wyszukaj zasoby po stronie
        4: Wyszukaj języki programowania
        5: Wyszukaj centra badawcze PWR
        6: Wyszukaj laboratoria
        7: Wygeneruj BibTeX-y dla obecnie wyszukanych zasobów
        8: Zapisz do pliku obecne BibTex-y
        9: Przetestuj pakiet package2
        10: Wyjście z programu'''


def search_by_author_id():
    """Drukuje wszystkie zasoby autora."""
    global entries
    ans = input("\nId autora: ")
    entries = api_handler.get_author_entries(ans, api_key)
    for entry in entries:
        print(entry)
    print(f'\nRazem {len(entries)} zasobow\n')


def search_by_author_id_and_page():
    """Drukuje wszystkie zasoby autora na danej stronie."""
    global entries
    ans = input("\nId autora: ")
    ans2 = input("\nStrona: ")
    entries = api_handler.get_author_entries_by_page(ans, api_key, ans2)
    for entry in entries:
        print(entry)
    print(f'\nRazem {len(entries)} zasobow\n')


def search_by_page():
    """Drukuje wszystkie zasoby z danej strony."""
    global entries
    ans = input("\nStrona: ")
    entries = api_handler.get_entries_by_page(api_key, ans)
    for entry in entries:
        print(entry)
    print(f'\nRazem {len(entries)} zasobow\n')


def search_centers():
    """Drukuje wszystkie centra badawcze nalezace do PWR."""
    try:
        centers = api_others.get_pwr_reseach_centres(api_key)
    except AttributeError:
        return "Nie ma takiej metody jak get_pwr_reseach_centres"
    for center in centers:
        print(center)
    return f'Znaleziono {len(centers)} centrow badawczych'


def search_lang():
    """Drukuje wszystkie języki programowania w bazie."""
    try:
        langs = api_others.get_programming_languages(api_key)
    except AttributeError:
        return "Nie ma takiej metody jak get_programming_languages"
    for lang in langs:
        print(lang)
    return f'Znaleziono {len(langs)} jezykow programowania'


def search_laboratories():
    """Drukuje wszystkie laboratoria."""
    try:
        labs = api_others.get_laboratories(api_key)
    except AttributeError:
        return "Nie ma takiej metody jak get_laboratories"
    for lab in labs:
        print(lab)
    return f'Znaleziono {len(labs)} laboratoriow'


def generate_bibtex():
    """Konwertuje obecne zasoby w pamieci na format BibTeX."""
    global bibtexes
    bibtexes = api_handler.get_entries_details(entries, api_key)
    print(f'\nWygenerowano razem {len(bibtexes)} BibTeX-ow\n')


def save_bibtex():
    """Zapisuje do pliku obecne w pamieci BibTeX-y."""
    with open("bibtex.bib", "a") as myfile:
        for item in bibtexes:
            myfile.write(item.get_bibtex() + '\n')
    print(f'\nZapisano razem {len(bibtexes)} BibTeX-ow\n')


def test_package2():
    """Testuje przykladowa metode z pakietu package2."""
    print(main.say_hello())


def _exit():
    """Wychodzi z programu."""
    sys.exit()


SWITCHER = {
    '1': search_by_author_id,
    '2': search_by_author_id_and_page,
    '3': search_by_page,
    '4': search_lang,
    '5': search_centers,
    '6': search_laboratories,
    '7': generate_bibtex,
    '8': save_bibtex,
    '9': test_package2,
    '10': _exit
}


def menu():
    ans = 0
    while(ans != 10):
        print(MENU)
        ans = input("\nCo chcesz zrobic?: ")
        SWITCHER[ans]()


def test_versioning():
    print(search_lang())
    time.sleep(1)
    print(search_centers())
    time.sleep(1)
    print(search_laboratories())


if __name__ == '__main__':
    menu()
