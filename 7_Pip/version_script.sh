#!/bin/bash
 
#pip3 install git+git://github.com/radosz99/azon-api-library.git@biblioteka#egg=azon-api-library
 
pip3 install --upgrade git+git://github.com/radosz99/azon-api-library.git@v3.0#egg=azon-api-library
 
echo ----------Wersja v3.0---------- >> results.txt
python3 main.py >> results.txt
 
pip3 install --upgrade git+git://github.com/radosz99/azon-api-library.git@v4.0#egg=azon-api-library
 
echo ----------UPGRADE-Wersja v4.0---------- >> results.txt
python3 main.py >> results.txt
 
pip3 install --upgrade git+git://github.com/radosz99/azon-api-library.git@v5.0#egg=azon-api-library
 
echo ----------UPGRADE-Wersja v5.0---------- >> results.txt
python3 main.py >> results.txt
 
pip3 install --upgrade git+git://github.com/radosz99/azon-api-library.git@v6.0#egg=azon-api-library
 
echo ----------UPGRADE-Wersja v6.0---------- >> results.txt
python3 main.py >> results.txt
 
pip3 install --upgrade git+git://github.com/radosz99/azon-api-library.git@v5.0#egg=azon-api-library
 
echo ----------DOWNGRADE-Wersja v5.0---------- >> results.txt
python3 main.py >> results.txt
 
pip3 install --upgrade git+git://github.com/radosz99/azon-api-library.git@v4.0#egg=azon-api-library
 
echo ----------DOWNGRADE-Wersja v4.0---------- >> results.txt
python3 main.py >> results.txt
 
pip3 install --upgrade git+git://github.com/radosz99/azon-api-library.git@v3.0#egg=azon-api-library
 
echo ----------DOWNGRADE-Wersja v3.0---------- >> results.txt
python3 main.py >> results.txt