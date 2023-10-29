# Testausdokumentti

Ohjelman testaus on suoritettu unittestillä. Testit löytyvät [testikansiosta](https://github.com/ThomasGrundstrom/algoritmit-ai-harjoitustyo/tree/main/src/testit) ja ne voi suorittaa ohjelman juurikansiossa komennolla *poetry run invoke test*.
Dijkstran algoritmi on testattu kartoilla, joissa kuljetaan kahdeksaan suuntaan vertaamalla algoritmilla saatujen polkujen pituuksia manuaalisesti laskettuihin optimaalisiin pituuksiin. JPS-algoritmia on testattu kahdella [Moving AI Lab](https://www.movingai.com/benchmarks/grids.html):n sivuilta löytyvällä kartalla. Valitsin JPS:n testausta varten kartat itse satunnaisesti kaikkien sivuilta löytyvien karttojen joukosta. JPS-algoritmin testauksessa toistettiin 100 kertaa seuraavat askeleet:

1. Valitse satunnaisesti kartalta paikat lähtö- ja maalipisteelle.
2. Laske pisteiden etäisyys käyttäen Dijkstran algoritmia.
3. Laske pisteiden etäisyys käyttäen Jump Point Search:ia.
4. Vertaa saatuja etäisyyksiä toisiinsa.


## Testikattavuus

Testikattavuusraportti tallennetaan htmlcov-kansion index.html-tiedostoon, kun projektin juurihakemistossa suoritetaan komento *poetry run invoke coverage-report*.

![](./kuvat/algoritmit-ai-testikattavuus.png)


## Koodin laatu

Koodin formalisointi on tehty autopep8:lla (juurihakemistossa komento *poetry run invoke format*) ja koodin laatua on ylläpidetty pylintin tarkistusten avulla (*poetry run invoke lint*)
