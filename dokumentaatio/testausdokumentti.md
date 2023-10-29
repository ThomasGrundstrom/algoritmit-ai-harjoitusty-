# Testausdokumentti

Ohjelman testaus on suoritettu unittestillä. Testit löytyvät [testikansiosta](https://github.com/ThomasGrundstrom/algoritmit-ai-harjoitustyo/tree/main/src/testit) ja ne voi suorittaa ohjelman juurikansiossa komennolla *poetry run invoke test*.
Dijkstran algoritmi on testattu kartoilla, joissa kuljetaan kahdeksaan suuntaan vertaamalla algoritmilla saatujen polkujen pituuksia manuaalisesti laskettuihin optimaalisiin pituuksiin. JPS-algoritmia on testattu kahdella [Moving AI Lab](https://www.movingai.com/benchmarks/grids.html):n sivuilta löytyvällä kartalla. Valitsin JPS:n testausta varten kartat itse satunnaisesti kaikkien sivuilta löytyvien karttojen joukosta. JPS-algoritmin testauksessa toistettiin 100 kertaa seuraavat askeleet:

1. Valitse satunnaisesti kartalta paikat lähtö- ja maalipisteelle.
2. Laske pisteiden etäisyys käyttäen Dijkstran algoritmia.
3. Laske pisteiden etäisyys käyttäen Jump Point Search:ia.
4. Vertaa saatuja etäisyyksiä toisiinsa.

Reitinhaun jälkeen algoritmit tulostavat komentoriville löytyneiden reittien pituudet sekä reittien löytämiseen kuluneet ajat. Tulostuneista aikatiedoista näkyy, että useimmissa tapauksissa JPS löytää optimaalisen reitin nopeammin kuin Dijkstran algoritmi. Tämä johtuu siitä, että Dijkstran algoritmissa reitinhaku kulkee jokaiseen suuntaan lähtösolmusta ja keskimäärin yhden ruudun käsittelyyn menee kauemmin kuin JPS:llä. Toisin kuin Dijkstran algoritmi, JPS etsii "hyppypisteitä", eli pisteitä, joiden läpi optimaalinen polku voisi mahdollisesti kulkea, ja laajentaa hakua vain niiden kohdalta. Lisäksi JPS ei kulje kaikkiin mahdollisiin suuntiin, vaan priorisoi reitinhakua maalipistettä kohti.


## Testikattavuus

Testikattavuusraportti tallennetaan htmlcov-kansion index.html-tiedostoon, kun projektin juurihakemistossa suoritetaan komento *poetry run invoke coverage-report*.

![](./kuvat/algoritmit-ai-testikattavuus.png)


## Koodin laatu

Koodin formalisointi on tehty autopep8:lla (juurihakemistossa komento *poetry run invoke format*) ja koodin laatua on ylläpidetty pylintin tarkistusten avulla (*poetry run invoke lint*)
