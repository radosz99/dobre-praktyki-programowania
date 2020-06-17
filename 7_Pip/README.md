Rezultat wygenerowania BibTeX-ów najlepiej widać [tutaj](https://github.com/radosz99/azon-api-library/blob/biblioteka/bibtex.bib).

Podsumowanie realizacji w pliku *RealizacjaPip.pdf*

# Description  
*biblioteka* - versioned library with few packages and few modules inside of each of them  [**--> MOVED TO GITHUB**](https://github.com/radosz99/azon-api-library)  
*master* - simple application using library from *biblioteka*  

- [x] Searching resources by author id and pages
- [x] Converting resources to BibTex (book, article, misc, phdthesis, techreport)
- [x] Saving resources in BibTex format to the .bib file
- [x] Some other methods
- [x] Final report
# Use info

Install package from GitHub:
```
$ pip install git+git://github.com/radosz99/azon-api-library.git@biblioteka#egg=azon-api-library
```
Change package version by changing VERSION (available versions can be viewed [here](https://github.com/radosz99/azon-api-library/releases)) and running this command:
```
$ pip install --upgrade git+git://github.com/radosz99/azon-api-library.git@VERSION#egg=azon-api-library
```