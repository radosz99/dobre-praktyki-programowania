# Instrukcje

## Lab01 - Git

26/02/20

Wstęp do systemu kontroli wersji Git. 

    Książka: https://git-scm.com/book/en/v2
    podstawowe komendy: https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html
    ssh: https://help.github.com/articles/connecting-to-github-with-ssh/
    https://rogerdudler.github.io/git-guide/index.pl.html?fbclid=IwAR393ICKKY9xunMezWSn3WHqH6BRTp3XCU83v4gYSAylcls6t_R9m4HZKYk

## Lab02 - Projekt grupowy

04/03/20

Wycieczki rowerowe

Wykorzystywane technologie: - Java 8-13 - JavaFX lub Swing - SQLite

Do projektu powinno być założone repozytorium kodu, a na nim gałęzie: master, develop oraz robocze gałęzie na zadania (issues).

Gałąź develop służyć ma do składowania roboczej wersji projektu, natomiast master powinna zawierać wersje projektu, które dają się już uruchamiać. Na gałęziach roboczych powstawać mają kody implementowanych funkcji. Gałęzie te powinny być merdżowane do gałęzi develop, gałąź develop zaś do gałęzi master.

Minimalne wymagania funkcjonalne:

Aplikacja powinna umożliwiać tworzenie, przeglądanie, edytowanie i usuwanie wycieczek.

Można pomyśleć o pracy aplikacji w dwóch kontekstach: planowania(gromadzenie informacji przed wycieczką)lub raportowanie (zdawania relacji z odbytej wycieczek).

Wycieczka to logicznie zbiór danych charakteryzowany przez: opis tekstowy, zdjęcia, tracki, uczestników, daty.

Aplikacja powinna umożliwiać ładowanie i eksportowanie wycieczek. Należy zaproponować, w jaki sposób spakowana jest wycieczka.

## Lab03 - Projekt grupowy cd.

11/03/20

Należy rozwinąć projekt zaczęty w trakcie laboratoriów poprzednich (lab02):

    w kodzie powinny być uwzględnione testy jednostkowe zaimplementowane z wykorzystaniem JUnit, Mockito itp. (proszę zastanowić się, jak oprogramować testy, gdy implementacja jest jeszcze niepełna - mowa tu o "mockowaniu", https://www.samouczekprogramisty.pl/testy-jednostkowe-z-uzyciem-mock-i-stub/)
    powinna pojawić się dokumentacja kodu javadoc (dokumentację należy umieścić gdzieś w drzewie projektu, w przyszłości przećwiczymy, jak generować taką dokumentację w sposób automatyczny w ramach CI)
    należy wykorzystać możliwość definiowania szablonów dla issues i merge requests (aby zapoznać się z tematem proszę sięgnąć do materiałów ukrytych pod linkami na podstronie: Systemy kontroli wersji (git, gitlab, github) i systemy śledzenia zagadnień (JIRA, Track, Mantis)#gitlab, w szczególności do description_templates i tego co skrywa sekcja .gitmessages)
    należy wykorzystać adresowanie komentarzy i opisów do członków zespołu za pomocą: @tutajNickLubKomenda (w efekcie można wrzucać wpisy do zestawienia todos https://about.gitlab.com/2016/03/02/gitlab-todos-feature-highlight/, https://docs.gitlab.com/ee/workflow/todos.html)

Generalnie celem laboratorium jest przećwiczenie dobrych praktyk stosowanych podczas pracy na współdzielonym repozytorium kodu oraz związanych z zapewnieniem jakości kodu (testowanie, dokumentacja).

Proszę rozdzielić zadania w grupie. W repozytorium na gitlabie powinny pojawić się efekty (będą sprawdzane opisy przy issues oraz merge requests).

UWAGA: z uwagi na problemy ze stabilnością działania usługi gitlab można (awaryjnie) przenieść projekt na inną usługę (np. github). Oczywiście wiąże się to z koniecznością założenia tam projektu i rozesłania zaproszeń.

## Lab04 - Mavenowe repozytorium

18/03/20

Zadanie realizowane ma być indywidualnie. Jego celem jest przećwiczenie możliwości współdzielenia bibliotek budowanych i wykorzystywanych w projektach mavenowych. Zadanie polegać ma na:

    stworzeniu projektu maven'owego na implementację biblioteki programowej służącej do "filtrowania" i "konkatenacji" plików CSV
        "filtrowanie" polegać ma na wybieraniu wierszy i kolumn podobnie jak można to zrobić korzystając za pomocą narzędzia awk (https://www.joeldare.com/wiki/using_awk_on_csv_files).
        "konkatenacja" polegać ma na łączeniu listy plików w jeden plik wynikow
    stworzeniu projektu maven'owego na implementację aplikacji korzystającej z wymienionej biblioteki
    zdeponowaniu zbudowanej biblioteki w repozytorium gitlab (w ten sposób zasymulowane zostanie zdalne repozytorium mavenowe) oraz pobraniu tej bibliotek z gitlaba podczas budowania aplikacji (w trakcie rozwijanie zależności zdefiniowanych w pliku pom.xml)

Linki:

    Link do tutoriala o wykorzystaniu gitlaba w roli mavenowego repozytorium: https://ubs-soft.com/maven-private-repository-in-gitlab/
    Link do materiałów związanych z tematem korzystania z mavena udostępnionych na niniejszej wiki: Praca nad projektem Java#Projekt mavenowy

Konwencja nazewnicza projektu na gitlabie i tworzonych na nim gałęzi:

    nazwa projektu INazwisko_Maven
    gałąź maven (do składowania zbudowanej biblioteki, ta gałąź jest traktowana jako repozytorium mavenowe - czyli zdalny katalog o odpowiedniej dla mavena strukturze)
    gałąź biblioteka (do składowania źródeł kodu biblioteki)
    gałąź aplikacja (do składowania źródeł kodu aplikacji korzystającej z biblioteki)

Słownik:

    artefakt — samoistna jednostka w projekcie, artefaktem jest np. każdy z modułów czy każda z zależności projektu. Można powiedzieć, że artefakt to takie zbiorcze określenie, które obejmuje projekty, moduły, biblioteki, pluginy (czyli elementy całego procesu), archetypy (coś w rodzaju ‘szablonu’ projektu, który możesz szybko skonfigurować i uruchomić) itd.
    pom.xml — główny plik z ustawieniami dla mavena w projekcie
    repozytorium — zbiór artefaktów. Każda instalacja mavena powoduje utworzenie lokalnego repozytorium. Podczas pracy z mavenem wykorzystywane są także repozytoria zdalne: centralne oraz pomocnicze, stworzone np. do obsługi jakichś projektów

Uwagi:

    Użycie gitlaba w roli repozytorium mavenowego może być zakwestionowane - wszak istnieją dedykowane repozytoria mavenowe. W zadaniu chodziło jednak o pokazanie możliwości współdzielenia tworzonych bibliotek, co daje się zrealizować w zaproponowany sposób.

## Lab05 - Systemy ciągłej integracji

25/03/20

Celem laboratorium jest przećwiczenie sposobu pracy z systemami ciągłej integracji. Do przetestowania są dwa dostępne rozwiązania: Gitlab CI oraz Jenkins.

    Jenkins to aplikacja webowa, którą można zainstalować lokalnie z pliku .war (rozwiązanie zalecane, sprawia mniej problemów konfiguracyjnych, ma mniejsze wymagania względem uprawnień). Można ją też pozyskać w postaci postaci obrazu dockerowego i uruchomić w kontenerze (rozwiązanie opcjonalne, może sprawić sporo problemów konfiguracyjnych, wymaga uprawnień administratora).

    Gitlab CI to funkcja gitlaba, która pozwala odpalać zadania na komputerze użytkownika (użytkownik musi mieć zainstalowanego, skonfigurowanego i uruchomionego gitlab runnera).

Zagadnienia związane z konfiguracją i uruchamianiem tych narzędzi opisano w materiale Systemy ciągłej integracji (Jenkins, gitlab CI/CD). Proszę go uważnie przestudiować !!!

Poczas realizacji zadania należy:

    skonfigurować projekt mavenowy na gitlabie by podczas rejestrowania zmian w repozytorium automatycznie wykonywała się kompilacja źródeł, uruchamiane były testy, tworzona była wersja dystrybucyjna (tj. wykonywalny jar). Ma przy tym zadziałać gitlab runner (po szczegóły dotyczące instalacji gitlab runnera można sięgnąć do, oprócz wymienionego wyżej materiałów, instrukcji dostępnej na stronie: https://docs.gitlab.com/runner/)
    skonfigurować projekt jenkinsowy by co jakiś czas (z zadanym interwałem) w jego ramach wykonywane były te samych kroki co podczas pracy gitlab runnera. Główna metodycznie różnica polegać ma na sposobie wyzwalania zadania. Tutaj zadanie wyzwalane ma być według harmonogramu. Zadanie to wykonywać ma komputer, na którym działa Jenkins. Zakładam, że będzie to komputer uczestniczącego w zajęciach.

Podczas realizacji zadania proszę wykorzystać kod źródłowy stworzony w trakcie poprzedniego laboratorium (w przypadku problemów z podłączaniem biblioteki można tę bibliotekę osadzić w projekcie aplikacji).

## Lab06 - Systemy recenzowania kodu

01/04/20

Zadanie polega na sprawdzeniu w praktyce jak może wyglądać proces recenzowania kodu z użyciem gerrita. Ogólnie mówiąc - trzeba uruchomić narzędzie i pokazać, że umie się z niego korzystać.

Gerrit to nakładka na gita (dokładniej - aplikacja webowa, która zarządza repozytorium kodu). Z jego pomocą można kontrolować wprowadzanie zmian do repozytorium. Odbywa się to, ogólnie mówiąc, w kilku etapach. Najpierw zgłaszana jest zmiana. Zmiana wisi na gerricie dopóki nie zostanie pozytywnie zrecenzowana - tj. dopóki nie uzyska wystarczającej liczby punktów. W trakcie recenzjowania zmiana może trafić do poprawki oraz ponownej oceny.

Gerrit nie ma zbyt przyjaznego graficznego interfejsu. Zaczyna w nim być coś widać, kiedy zmian zaczyna przybywać. Proszę się więc nie przerażać podczas pierwszego kontaktu z tym narzędziem.

Realizacja zadania polegać ma na:

    uruchomieniu gerrita
    stworzeniu repozytorium kontrolowanego przez gerrita
    wprowadzeniu do repozytorium zmiany
    zrecenzowaniu zmiany (wraz z komentarzem)
    utrwaleniu zmiany w repozytorium

Proszę spróbować wprowadzić zmiany kilka razy. Proszę spróbować zrecenzować kod przyjmując role różnych użytkowników (recenzja odbywa się za pośrednictwem webowego interfejsu gerrita - trzeba więc w nim utworzyć konta użytkowników). Proszę zobaczyć, jak wyglądają komentarze, jaki jest efekt odrzucenia zmiany, kiedy zmiana zostaje zatwierdzona.

W sumie dobrze byłoby mieć gerrita hostowanego na jakimś serwerze. Ale to wymagałoby zewnętrznych zasobów. Dlatego proszę o uruchomienie gerrita lokalnie (na własnym komputerze). Gerrita można uruchomić z pliku .war (co zalecam) lub jako obraz dockerowy (co może sprawić więcej kłopotu).

Do rozliczenia zadania proszę utworzyć na gitlabie nowe repozytorium o nazwie gerrit (w istniejącej grupie projektów). Do tego repozytorium (do gałęzi master) proszę wstawić zrzuty z ekranu wraz z opisem, co przedstawiają i na jakim etapie procesu je zrobione. Opisy i zrzuty powinny obrazować jak założono repozytorium, jak zgłaszano zmiany, jak wyglądała recenzja. Proszę to potraktować jak polecenie przygotowanie małego tutoriala.

W trakcie laboratorium proszę użyć źródeł kodu z lab04. Wystarczy użyć kod aplikacji (w trakcie zajęć nie trzeba tworzyć żadnych nowych programów - chodzi raczej o przetestowanie działania narzędzia do recenzowania kodu).

Więcej informacji o gerricie i podpowiedzi pomocnych podczas realizacji zadania można znaleźć

    w sekcji Systemy recenzowania kodu (gerrit) (proszę zajrzeć pod opis idei funkcjonowania gerrita)
    w materiale udostępnionym na webdysku: https://webdysk-ng.e-science.pl/filelist/zdpp/Team/gerrit01.pdf

Ten drugi szczególnie polecam (koniecznie należy się z nim zapoznać).

## Lab07 - Python

08/04/20

Od tego laboratorium następuje zmiana platformy programowej. Zamiast Javy należy korzystać z Pythona.

Napisz program w Pythonie, który pozwoli znaleźć miejsce na planszy scrabble dla wyrazu zbudowanego z wylosowanych przez użytkownika liter. Zakładamy, że plansza oraz jej zajętość (układ już obecnych na niej wyrazów) jest jednym z parametrów implementowanej metody, drugim zaś - zestaw liter użytkownika. Wynikiem działania metody jest zmiana układu wyrazów na planszy (dodany nowy wyraz) oraz zmieniona lista liter użytkownika. Tak więc oczekiwane jest dostarczenie algorytmu, który pozwoli na realizację jednego ruchu w grze scrabble. Nie trzeba implementować całej gry. Wystarczy też, by stworzone rozwiązanie działało w trybie konsolowym (na ekranie ma być wyświetlany za pomocą znaków układ wyrazów na planszy przed i po wykonaniu ruchu).

Algorytm znajdujący położenie dla nowego wyrazu wcale nie jest prosty. Najpierw trzeba stworzyć z dostępnych liter wyraz, a potem trzeba wpasować go w odpowiednie miejsce na planszy mając na uwadze jak największą liczbę zdobywanych punktów. Można pominąć kwestię blokowania przy tym możliwości zdobycia punktów przez przeciwnika.

Tego typu zadania zaliczane są do zadań kombinatorycznych (a więc bardzo złożonych obliczeniowo). Można podczas implementacji zastosować pewne uproszczenia - np. można skorzystać z gotowych słowników wyrazów (dostępnych on-line lub pobranych lokalnie). Można też pominąć kryterium zdobycia największej liczby puntów pozostając tylko przy znalezieniu miejsca na najdłuższy wyraz, jaki można stworzyć z liter użytkownika.

Do celów testowych można przyjąć, że ustawienie początkowe planszy będzie podawane z pliku (aby za każdym razem nie wprowadzać nowych danych). Zestaw liter na planszy oraz zestaw liter użytkownika powinien być zgodny z regułami scrabble.

Zalecanym środowiskiem developerskim jest PyCharm (ale każde inne też będzie dobre, np. VS Code).

## Lab08 - Python + Flask

15/04/20

Napisz aplikację z restowym endpointem mogącą pełnić rolę backendu do systemu umożliwiającego grę w scrabble on-line. Zaprojektowane API powinno wystarczyć do:

    zinicjowania gry (parametrem jest liczba uczestników),
    losowania liter (z puli przewidzianej w regułach scrabble),
    zapamiętywania stanu planszy, pilnowania sekwencji ruchów,
    zakończenia gry.

Implementacja bardziej zaawansowanej logiki nie jest wymagana (nie trzeba sprawdzać poprawności ruchów, nie trzeba wyliczać punktów).

Aplikacja powinna przechowywać dane (stan gry): w pamięci, w pliku oraz (opcjonalnie) w bazie danych (w pamięci, na dysku, jako osobny serwis). Wyróżnienie tych miejsc składowania danych jest celowe. Chodzi w nim o wykazanie, że szybkość generowania odpowiedzi z serwisu zależy mocno od sposobu jego implementacji (dostęp do pamięci operacyjnej powinien być szybki, dostęp do zasobów dyskowych zaś może być powodem znacznych opóźnień). Testy obciążeniowe przewidziano na kolejne zajęcia.

Proszę przygotować tak aplikację webową, by dało się ją skonfigurować (albo przez pliki konfiguracyjne, albo też przez uruchomienie odpowiedniej restowej metody konfigurującej serwis). Zalecane jest użycie frameworku Flask (Python).

Tutoriale:

    1. https://auth0.com/blog/developing-restful-apis-with-python-and-flask/ 
    2. https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-1-fae9ff66a706 
    3. https://dzone.com/articles/restful-web-services-with-python-flask https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way 

## Lab09 - JMeter

22/04/20

Zadanie polega na przetestowaniu restowych endpointów aplikacji napisanej w trakcie lab08 z wykorzystaniem narzędzia JMeter.

Podczas realizacji zadania należy:

    pobrać i zainstalować na własnym komputerze JMeter,
    zdefiniować i przeprowadzić testy obciążeniowe restowych endpointów stworzonej aplikacji,
    opisać wykonane prace, dokonując przy tej okazji omówienia otrzymanych rezultatów testów.

Planowane testy obciążeniowe powinny być parametryzowane danymi testowymi (podczas przeprowadzania testu dane te powinny odczytywane z pliku i wstawiane w zapytania). Proszę przeprowadzić testy przy różnych trybach uruchomienia aplikacji (wykonując lab08 należało tak przygotować aplikację, by można ją było uruchomić w trybie przechowywania danych w pamięci, w pliku i opcjonalnie - w bazie danych). Same testy też powinny być uruchamiane przy różnych ustawieniach (liczba użytkowników, częstość zapytań itp.). Oczywiście testy będą miały sens, jeśli biznesowa logika ukryta za endpointem będzie robiła coś konkretnego.

Jako wynik zadania należy dostarczyć: raport z opisem wykonanych prac (dokument pdf), zapamiętane plany testów (pliki .JMX), wykorzystane dane testowe (pliki csv). Premiowany będzie sposób omówienia wyników testów oraz wyciągnięte wnioski. Artefakty te proszę umieścić na gitlabie w projekcie o nazwie INazwisko_JMeter (w swojej grupie projektów DPP). Proszę nie zapomnieć o samoocenie.

Poniżej zestawiono kilka przydatnych linków:

    https://www.javatpoint.com/jmeter-tutorial (niezły opis tego, czym jest JMeter, jak z niego korzystać, ze zrzutami z ekranu) 
    https://octoperf.com/blog/2018/03/29/jmeter-tutorial/ 
    https://stackoverflow.com/questions/27634885/in-jmeter-what-would-be-syntax-of-parameters-in-body-data-section-of-http-reque 
    https://github.com/department-of-veterans-affairs/ascent-sample/wiki/QA-:-Performance-Test-Plan-using-JMeter (tutaj wspomina się o rozszerzeniu "dashboard generator", które pozwala na wyświetlanie ładnych wykresów) 

## Lab10 - Python+pip

29/04/20

Podczas laboratorium należy przećwiczyć:

    korzystanie z tokenów podczas komunikacji z usługami sieciowymi poprzez restowe API oraz
    posługiwanie się pakietami w pythonie.

Jeśli chodzi o punkt pierwszy (wykorzystanie tokenów), to zasada jest prosta - do każdego żądania wysłanego do usługi należy dołączyć token. Token ten należy wcześniej pozyskać od dostawcy usługi. Wykorzystaną usługą ma być restowe API systemu AZON. Poprzez to restowe API należy pozyskać informacje o zdeponowanych zasobach. Do wysyłania zapytań oraz przetwarzania odpowiedzi ma służyć stworzona biblioteka (patrz opis dalej).

Aby uzyskać token wystarczy o niego wystąpić, wypełniając formularz dostępny na stronie: https://api.e-science.pl/ (do tej strony można dojść z systemu AZON, podstrona narzędzia: https://zasobynauki.pl/narzedzia/). Proszę taki formularz wypełnić, aplikując o token standardowy. Może okazać się, że token nie przyjdzie od razu. Proszę sięgnąć do instrukcji udostępnionej pod linkiem po szczegółowe informacje: https://zasobynauki.pl/podr%C4%99czniki%20u%C5%BCytkownika/Instrukcja_AZON_fAfiPGW.pdf (opisano tam, patrz Rozdział 3, jak korzystać z tokena, wskazano również miejsce, skąd można pozyskać swaggerow opis API).

Jeśli chodzi o posługiwanie się pakietami, to tu nie ma żadnej specjalnej niespodzianki. Python, podobnie jak inne języki programowania, pozwala na tworzenie bibliotek oprogramowania dystrybuowanych w formie pakietów. I podobnie do innych platform, pakiety te mogą być składowane w zdalnych repozytoriach.

Pakiety pythonowe mogą być tworzone na kilka sposobów (source tree, source distribution, wheel). Terminy z tym związane zacytowano poniżej.

Binary Distribution
    A specific kind of Built Distribution that contains compiled extensions. 

Built Distribution
    A Distribution format containing files and metadata that only need to be moved to the correct location on the target system, to be installed. Wheel is such a format, whereas distutil’s Source Distribution is not, in that it requires a build step before it can be installed. This format does not imply that Python files have to be precompiled (Wheel intentionally does not include compiled Python files). 

Distribution Package
    A versioned archive file that contains Python packages, modules, and other resource files that are used to distribute a Release. The archive file is what an end-user will download from the internet and install. 
    A distribution package is more commonly referred to with the single words “package” or “distribution”, but this guide may use the expanded term when more clarity is needed to prevent confusion with an Import Package (which is also commonly called a “package”) or another kind of distribution (e.g. a Linux distribution or the Python language distribution), which are often referred to with the single term “distribution”. 

Egg
    A Built Distribution format introduced by setuptools, which is being replaced by Wheel. For details, see The Internal Structure of Python Eggs and Python Eggs 

Wheel
    A Built Distribution format introduced by PEP 427, which is intended to replace the Egg format. Wheel is currently supported by pip. 

Pakiety muszą też charakteryzować się pewną strukturą. Proszę zapoznać się z informacjami udostępnionymi na stronach:

    https://www.bernat.tech/pep-517-and-python-packaging/
    https://packaging.python.org/overview/
    https://packaging.python.org/tutorials/packaging-projects/
    https://packaging.python.org/guides/distributing-packages-using-setuptools/
    https://www.digitalocean.com/community/tutorials/how-to-package-and-distribute-python-applications
    https://code.tutsplus.com/tutorials/how-to-write-package-and-distribute-a-library-in-python--cms-28693
    https://code.tutsplus.com/tutorials/how-to-write-your-own-python-packages--cms-26076
    https://packaging.python.org/discussions/wheel-vs-egg/
    https://pip.pypa.io/en/latest/user_guide/#installing-from-wheels
    https://packaging.python.org/glossary/#term-wheel

Do realizacji ćwiczenia szczególnie pomocne będą materiały udostępnione na githubie (proszę je wykorzystać):

    https://github.com/BillMills/pythonPackageLesson


Zadanie do wykonania jest następujące:

    Stwórz w języku python bibliotekę składającą się z pakietów i modułów. Pakietów musi być przynajmniej dwa, a w każdym ma być kilka modułów. Nie muszą one być zbyt obszerne, ale nie mogą być też zbyt małe. Mają one zawierać klasy pozwalające wysyłać zapytania do AZONu poprzez restowe API (z tokenem) oraz przetwarzać wyniki tych zapytań.
    Powiel bibliotekę w kilku wersjach. Niech każda kolejna wersja biblioteki różni się jakimś szczegółem, np. listą atrybutów jakiejś metody w jakimś module. Zamieść te kilka wersji biblioteki na gitlabie w gałęzi biblioteka (trochę podobnie jak to było z biblioteką mavenową - nie korzystamy z dedykowanych repozytoriów PyPi, tylko z własnego - w przypadku problemów można spróbować zadziałać z jakimś lokalnym repozytorium pakietów).

Celem jest sprawdzenie, jak to jest z zależnościami w projekcie aplikacji (patrz następny podpunkt) przy upgradzie lub downgradzie biblioteki. Proszę spróbować zmienić zależność w projekcie aplikacji na nowszą i starszą wersję biblioteki (niech zmiany będą przetestowane w obu kierunkach).

    Stwórz nowy projekt aplikacji, w którym zostanie wykorzystana biblioteka (umieszczając źródła kodu projektu jak zwykle na gitlabie - niech to będzie gałąź aplikacja). Aplikacja (może działać tylko w trybie konsolowym), która ma powstać w tym projekcie ma pozwolić na:
        wyszukiwanie zasobów po ich autorze,
        generowanie metadanych wyszukanych zasobów w formacie bibtex (patrz: https://pl.wikipedia.org/wiki/BibTeX).
    W azonowym API jest sporo zdefiniowanych metod i endpointów. W szczególności proszę zacząć od Entry - tam można pozyskać podstawowe dane dotyczące zasobu.
    Wynik (aplikacja, biblioteka oraz opis wykonanych prac) umieść na gitlabie w repozytorium: INazwisko######_DPP_Python_pip w odpowiedniej grupie.


Porady:

    Wygenerowanie paczek do dystrybucji:

	python setup.py sdist bdist_wheel

    Dekompilator (dodane przy okazji): https://docs.python.org/2/_sources/library/dis.rst.txt

    Zainstalowanie biblioteki w projekcie:

	pip install ../freezing/dist/pathology-0.2-py3-none-any.whl 


    Wykorzystanie gita jako repozytorium pakietów (proszę dostosować do odpowiedniej gałęzi, może być problem z certyfikatami/kluczami)!!!!):

#git push --set-upstream git@git.e-science.pl:etkubik/package-example.git master (jeśli repozytorium zdalne istnieje)

# gitlab ver.10:     git remote add origin git@git.e-science.pl:etkubik/package-example.git

# (w konsoli jako alternatywa do działania bezpośrednio w pyCharm)
# cd sciezka_do_projektu 
source venv/bin/activate
# (po utworzeniu kodu włączenie wersjonowania: git init, git add, git commit)
# (wrzucenie projektu na gitlab - wymaga wcześniejszego utworzenia projektu na gitlabie)
git remote add origin git@git.e-science.pl:etkubik/package-example.git
git push -u origin --all
git push -u origin --tags
# instalacja biblioteki pobranej z gitlaba dla nowego projektu w lokalnym venv
pip install git+ssh://git@git.e-science.pl/etkubik/package-example.git#egg=package-example

    Tutorial m.in. o tym, jak zainstalować własny serwer pypi: http://docs.python-guide.org/en/latest/shipping/packaging/ . Opisano w nim:

a) wykorzystanie SimpleHTTPserver do serwowania pakietów przez umieszczenie ich w katalogach

(python2) python -m SimpleHTTPServer 9000
(python3) python -m http.server

potem można już instalować pakiety:

pip install --extra-index-url=http://127.0.0.1:9000/ MyPackage
pip install  http://127.0.0.1:9000/MyPackage.tar.gz

Źródła:

    https://medium.com/knerd/best-practices-for-python-dependency-management-cc8d1913db82
    https://packaging.python.org/tutorials/managing-dependencies/
    https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1
    https://docs.pipenv.org/
    https://docs.pipenv.org/basics/
    http://snoozy.ninja/python/Package-Management/
    http://snoozy.ninja/python/Package-Management-Part-Two/

    https://setuptools.readthedocs.io/en/latest/setuptools.html
    https://caremad.io/posts/2013/07/setup-vs-requirement/

    https://media.readthedocs.org/pdf/pipenv/stable/pipenv.pdf
    https://docs.python.org/3/installing/
    https://packaging.python.org/tutorials/distributing-packages/
    https://python-packaging.readthedocs.io/en/latest/minimal.html
    https://gemfury.com/help/pypi-server/

## Lab11 - Python+Selenium web driver

06/05/20

Ważnym typem testów, którymi sprawdza się działanie aplikacji, są testy regresyjne (zobacz: https://testerzy.pl/baza-wiedzy/testy-regresji). Zwykle tego typu testy polegają na sprawdzaniu, czy aplikacja działa tak samo przed i po wprowadzeniu zmian, czy wprowadzone zmiany nie spowodowały pojawienia się nowych błędów lub czy nie ujawniły się błędy do tej pory ukryte. Uruchomienie testów regresyjnych może również posłużyć do weryfikacji, czy przypadkiem dane, z jakich korzysta aplikacja, nie zostały zmodyfikowane. Generalnie zastosowań idei testów regresyjnych może być wiele, między innymi takie, jakie określono w treści zadania do wykonania. Zadanie to brzmi tak:

    Korzystając z Selenium IDE oraz Selenium WebDriver (python) zaprojektuj i wykonaj testy regresyjne wybranej aplikacji webowej (Selenium IDE powinno być znane z innych kursów, Selenium WebDriver prawdopodobnie nie był omawiany na innych kursach).
    Testy mogą sprawdzać, przykładowo, czy przypadkiem nie zmieniono cen na jakieś wybrane artykuły (jeśli testowana aplikacja jest sklepem internetowym), czy nie pojawiły się jakieś zmiany na tablicy przylotów (jeśli testowana aplikacja dostarcza informacji o statusie lotów) itp. Aplikacja uruchamiająca testy musi posiadać jakieś miejsce do przechowywania danych (bo na podstawie porównania zapisanych danych z danymi nowo pozyskanymi można ocenić, czy doszło do jakiejś zmiany).
    Oczekiwanymi wynikami laboratorium (zamieszczanymi w repozytorium git o nazwie INazwisko####_Selenium w grupie DPP) powinny być:
        Scenariusz Selenium IDE
        Kod źródłowy aplikacji służącej do uruchamiania testów z wykorzystaniem Selenium WebDriver
        Opis wykonanych prac i podsumowanie wyników (w pliku Readme.md razem z podpiętymi obrazkami)

Pewnym problemem może okazać się wybór aplikacji do testowania. Często aplikacje są zabezpieczane captchą lub stroną logowania (nie mówiąc już o systemach obserwujących wrogi ruch w sieci, które mogą zablokować całe domeny, ze środka których następują ataki - proszę więc nie przesadzać z tym testowaniem, by nie trafić na czarne listy podejrzanym o atak DDOS). Często też budowane są dynamicznie - co czasem trudno obsłużyć w Selenium WebDriver. W takich przypadkach można podjąć próbę wykorzystania aplikacji webowych służących do testowania zapytań (są wystawiane w Internecie właśnie do tego celu). Ostatecznie można spróbować podpiąć się pod jakąś lokalnie postawioną aplikację webową.

Ciekawym przypadkiem byłoby napisanie aplikacji testującej wskazane serwisy webowe zgodnie z jakimś harmonogramem zarządzanym przez Jenkinsa. Ale to nie jest wymagane na laboratorium.

    źródła: 
    1. https://www.seleniumhq.org/ (strona domowa projektu Selenium) 
    2. https://github.com/mozilla/geckodriver/releases (strona drivera do Mozilla/Firefox) 
    3. https://www.ultimateqa.com/best-test-automation-websites-to-practice-using-selenium-webdriver/ (linki do aplikacji webowych przeznaczonych do przeprowadzania testów, w szczególności do http://magento.softwaretestingboard.com/) 
    4. https://github.com/upgundecha/learnsewithpython (kody źródłowe towarzyszące książce: Learning Selenium Testing Tools with Python. Packt Publishing, 2014) 

## Lab12 - Python+Native

13/05/20

Tworzenie aplikacji w pythonie opiera się głównie na pisaniu kodu w tym właśnie języku. Istnieje jednak możliwość wykorzystania funkcji zaimplementowanych w innych językach programowania (C/C++, kod asemblera), skompilowanych do kodu maszynowego i udostępnionych w postaci bibliotek ładowanych dynamicznie. Takie natywne wsparcie przydaje się w wielu zastosowaniach.

Kod natywny można podpiąć do pythonowego projektu na kilka sposobów. Można o nich przeczytać na stronach:

    http://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/c++-wrapping.html
    https://blog.conan.io/2016/04/12/Extending-python-with-C-or-C++-with-pybind11.html
    https://docs.python.org/3/extending/extending.html#a-simple-example

Dobre przykłady opisano w książce "Python Journey from Novice to Expert" (moduły ctypes oraz CFFI oraz Native C/C++ extensions). Ich źródła kodu można znaleźć na githubie:

    https://github.com/PacktPublishing/Python-Journey-from-Novice-to-Expert/tree/master/Module%203/14_c_and_cpp_extensions

Ponadto ciekawą możliwością jest zbudowania pythonowych aplikacji w wersjach wykonywalnych (wersjach dystrybucyjnych). Tak zbudowane aplikacje mogą być zainstalowane na komputerze użytkownika oraz uruchamiane jak zwykłe programy, bez konieczności instalacji pythonowego interpretera. Z budowaniem wykonywalnych aplikacji wiąże się termin zamrażania aplikacji (kojarzy się z nim też tworzenie instalatorów). O zamrażaniu aplikacji można poczytać na stronach:

    http://docs.python-guide.org/en/latest/shipping/freezing/#freezing-your-code-ref
    https://cyrille.rossant.net/create-a-standalone-windows-installer-for-your-python-application/
    http://pynsist.readthedocs.io/en/latest/index.html

Zadanie do wykonania:

    Utwórz pakiet z metodami natywnymi służącymi do rozwiązywania układu równań liniowych (kod natywny nie musi być autorski, chodzi tu głównie o to, by połączyć kod natywny z kodem pythonowym). Zbuduj jego wersję dystrybucyjną.
    Wykorzystaj ten pakiet we własnej aplikacji parametryzowanej danymi wejściowymi pobieranymi z pliku (w pliku powinny znajdować się dane opisujące rozwiązywany układ równań liniowych).
    Stwórz wersję dystrubucyjną/wykonywalną aplikacji (przeznaczoną do uruchomienia pod Windows lub Linux).
    Stwórz instalator aplikacji (opcjonalnie).
    Wyniki (projekt pythonowy, kody biblioteki natywnej, wersja wykonywalna aplikacji, raport z opisem) zamieść w repozytorium INazwisko####_PythonNative w odpowiedniej grupie.


Porady:

    Instalacja niezbędnych zależności dla kompilatora C/C++

	sudo apt-get install python-dev
	sudo apt-get install python3-dev /// build-essential libssl-dev libffi-dev 

    Przykład załadowania i użycia standardowej biblioteki c (za pomocą ctypes):

import ctypes
ctypes.cdll
libc = ctypes.cdll.LoadLibrary('libc.so.6')
libc
libc.printf
cdll.LoadLibrary(util.find_library('libc'))

    Zamrożenie aplikacji

pip install pyinstaller

pyinstaller -F aaa.py

## Lab13 - TestLink

20/05/20

Testowanie powinno być nieodłączną częścią każdego poważniejszego projektu informatycznego. Dopóki rozmiar projektu jest niewielki prowadzenie testów nie nastręcza specjalnych trudności. Jednak gdy projekt staje się duży pojawia się potrzeba zarządzania testami.

Do zarządzania testami można wykorzystać różne narzędzia programowe. Jednym z bardziej znanych w środowisku open-source jest TestLink. Narzędzie to udostępnia graficzny interfejs użytkownika w formie aplikacji webowej prezentowanej w oknie przeglądarki. Poprzez ten interfejs można tworzyć projekty, deklarować plany testów, definiować przypadki testowe itd. Ponadto TestLink dostarcza API umożliwiające wymianę danych. Dzięki temu API zewnętrzne aplikacje mogą komunikować się z tym narzędziem, a w szczególności mogą przesyłać mu wyniki testów wykonywanych automatycznie.

Celem laboratorium jest poznanie specyfiki zarządzania testami z wykorzystaniem TestLinka. Zadanie do wykonania polega na:

    Uruchomieniu TestLinka
    Stworzeniu projektu, planu testów, przypadków testowych, specyfikacji budowanej wersji/wydania
    Uruchomieniu testów (wykonaniu przypadków testowych ręcznie i automatycznie)
    Wygenerowaniu raportu

Na wiki umieszczono materiał z opisem pierwszych kroków podczas pracy z TestLinkiem: Media:TestLink01.pdf. Są w nim fragmenty kodu (przesyłające wyniki testów do TestLinka) oraz linki do tutoriali (w tym do polecanego: https://www.guru99.com/testlink-tutorial-complete-guide.html)

Szczegółowe wymagania dotyczące sposobu realizacji zadania:

    Opisy projektu, planu testów oraz przypadków testowych nie powinny być ograniczone do jednego zdania. Proszę potraktować je jako elementy dokumentacji projektowej. Można myśleć o tej dokumentacji jako o dokumentacji Lab13 - projektu informatycznego uruchomionego na potrzeby realizacji kursu DPP. Podczas oceniania zadania będzie brana pod uwagę jakość tych opisów.
    Przypadki testowe powinny składać się z kilku kroków. Towarzyszący im opis powinien dać testerowi pełną wiedzę na temat tego, co ma zrobić, by przeprowadzić test (gdzie ma kliknąć i co ma otrzymać jako wynik - jeśli test jest wykonywany ręcznie lub co ma uruchomić - jeśli test ma być uruchomiony automatycznie).
    W pakiecie testów można zamieścić przypadki testowania własnej aplikacji napisanej na którymś z wcześniejszych laboratoriów. Przynajmniej jeden test musi być wykonany automatycznie (trzeba dołożyć implementację testu oraz uruchomienia testu z przesłaniem wyniku do TestLinka)
    W pakiecie testów można zamieścić przypadki testowania jakiejś zewnętrznej aplikacji (choćby strony wiki na e-science.pl). Tutaj można zostać przy testach wykonywanych ręcznie. Można też uruchomić testy za pomocą Selenium i przesłać wyniki do TestLinka.
    Testowanie wystarczy przeprowadzić dla jednej budowanej wersji (nie trzeba symulować uruchamiania testów dla kolejnych wydań)
    Jako wynik zadania należy dostarczyć raport (dokument pdf) z komentarzem, zrzutami opisów oraz wygenerowanymi raportami z przeprowadzonych testów. Raport powinien pojawić się w repozytorium INazwisko####_TestLink w odpowiedniej grupie.

## Lab14 Python + Jenkins + Testlink

27/05/20

Celem laboratorium jest przetrenowanie scenariusza, w którym

    Jenkins będzie uruchamiał testy jednostkowe dla aplikacji napisanej w języku python pobierając źródła kodu znajdujące się na gitlabie.
    Jenkins będzie publikował wyniki testów w Testlinku, w którym wcześniej zdefiniowano projekt z przypadkiem testowym uruchamianym automatycznie.

Wyniki laboratorium powinny być zamieszczone w repozytorium INazwisko####_Jenkins_Testlink podpiętym w odpowiedniej grupie DPP. Oczekiwane wyniki laboratorium to:

    Kod aplikacji z testami jednostkowymi (może ty być rozwijana wcześniej aplikacja webowa przy wykorzystaniu biblioteki flask) w gałęzi sources
    Raport o wykonaniu zadania (Readme.md) z podpiętymi obrazkami, na których widać: efekt działania jenkinsa (log z wykonania Jenkinsfile), efekt wrzucenia wyniku testu do Testlina (zrzut z testlinka, na którym widać wynik wykonania testu automatycznego)
    Uzupełnienia (można podać więcej szczegółów, jak wykonano zadanie).
