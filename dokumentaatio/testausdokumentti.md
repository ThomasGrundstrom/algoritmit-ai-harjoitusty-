# Testausdokumentti

Ohjelman testaus on suoritettu unittestillä. Testit löytyvät [testikansiosta](https://github.com/ThomasGrundstrom/algoritmit-ai-harjoitustyo/tree/main/src/testit) ja ne voi suorittaa ohjelman juurikansiossa komennolla *poetry run invoke test*.


## Testikattavuus

Testikattavuusraportti tallennetaan htmlcov-kansion index.html-tiedostoon, kun projektin juurihakemistossa suoritetaan komento *poetry run invoke coverage-report*.



## Koodin laatu

Koodin formalisointi on tehty autopep8:lla (juurihakemistossa komento *poetry run invoke format*) ja koodin laatua on ylläpidetty pylintin tarkistusten avulla (*poetry run invoke lint*)
