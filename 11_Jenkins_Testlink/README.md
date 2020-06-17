# Projekt Freestyle
Projekt można by skonfigurować w zwykłym pipeline, wykorzystując kod z poprzednich laboratoriów i wysyłając wyniki testów do Testlinka dokładnie w taki sam sposób, tylko że tym razem wywołując skrypt z poziomu Jenkinsa.
Postanowiłem skonfigurować go w projekcie typu *freestyle*, w którym można wykorzystać jenkinsowy plugin testlink.
## Konfiguracja krokow w Jenkinsie
Ważnym elementem było dodanie odpowiednich custom field'ów przy konfiguracji w Jenkinsie
![ss](screenshots/conf_jenkins.png)


## Konfiguracja test case'ow w Testlinku
I odpowiednio w Testlinku:
![ss](screenshots/conf_testlink.png)


## Wykonane testy w Jenkinsie
Poniżej prezentuje historię egzekucji poszczególnych testów. Zostały wykonane z użyciem Selenium WebDrive'ra.
![ss](screenshots/jenkins.png)

## Rezultaty w Testlinku

### 1 test
![ss](screenshots/tp3.png)

### 2 test
![ss](screenshots/tp4.png)


### 3 test
![ss](screenshots/tp5.png)

### 4 test
![ss](screenshots/tp6.png)
