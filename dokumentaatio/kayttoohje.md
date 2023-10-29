# Käyttöohje


## Kartan lisääminen

Ohjelman käyttämää karttaa voi muokata kartta.py-tiedostossa.
- Polku tiedostoon ohjelman juuresta: --> src --> kartta --> kartta.py

Tiedostossa voi luoda vapaavalintaisen kokoisen kartan muodostamalla kaksiulotteisen listan seuraavalla tavalla:
1. Luo lista.
2. Lisää luodun listan sisälle listoja, jotka sisältävät nollia (0) tai kolmosia (3). Nollat vastaavat tyhjiä ruutuja ja kolmoset vastaavat esteruutuja, joiden läpi ei saa kulkea. **Näiden "sisäisten listojen" tulee kaikkien olla yhtä pitkiä**
3. Lopputuloksena saadaan matriisi, jonka rivit ja sarakkeet muodostavat kartan. Kartan leveys määrittyy sarakkeiden määrän mukaan ja korkeus rivien määrän mukaan. Kartan visualisoinnin takia on suositeltavaa, että rivejä olisi korkeintaan 100 ja sarakkeita korkeintaan 180.
4. Valitse kartalta jokin alkupiste ja vaihda valitussa kohdassa olevan numeron tilalle 1.
5. Valitse kartalta loppupiste ja vaihda loppupisteen kohdalla olevan numeron tilalle 2.


### Huomioitavia asioita kartan luomisessa:

- **Jos et ole varma siitä, minkä näköinen tiedostossa luomasi kartta on, sen ulkonäköä voi tarkastella riippuvuuksien asentamisen jälkeen käynnistämällä ohjelman. Tiedosto kartta.py sisältää valmiiksi joitakin esimerkkikarttoja, jotka saa käyttöön poistamalla niiden edestä #-merkit.**
- **Ohjelman käynnistyttyä pygamen näytölle piirtyvässä kartassa vihreä ruutu on lähtöruutu, punainen on maaliruutu, harmaat ruudut ovat tyhjiä ruutuja ja mustat ruudut ovat esteruutuja.**
- Suositeltava kartan maksimileveys on 180 ja -korkeus 100.
- Jos valittujen lähtö- ja maaliruutujen välille ei ole mahdollista luoda polkua, ohjelma tulostaa tiedon tästä, eikä piirrä kartalle mitään.
- Jos kartta.py-tiedostoon ei tehdä mitään muutoksia, oletuksena tuleva kartta on 180 ruutua leveä ja 100 ruutua korkea, eikä sisällä yhtään esteitä. Oletuskartalla lähtöruutu on vasemmassa yläkulmassa ja maaliruutu oikeassa alakulmassa.


## Ohjelman käynnistäminen

- Asenna riippuvuudet komennolla *poetry install*
- Käynnistä ohjelma komennolla *poetry run invoke start*


## Reitinhaku kartalla

**Huom! Polkujen laskettu pituus muodostuu seuraavasti:**
- Kun siirrytään ruudusta toiseen joko vertikaalisesti tai horisontaalisesti, polun pituuteen lisätään 1.
- Kun siirrytään ruudusta toiseen diagonaalisesti, polun pituuteen lisätään sqrt(2).

Reitinhaun lähtöruudusta maaliruutuun voi toteuttaa kahdella eri algoritmilla: 

1. Dijkstran algoritmi: Paina näppäimistöllä d-näppäintä. Kartalle piirtyy sinisistä ruuduista muodostuva optimaalisen pituinen reitti alku- ja maaliruutujen välille. Komentoriville tulostuu tieto siitä, kuinka kauan reitinhaku kesti ja kuinka pitkä muodostettu polku on. Jos tahdot nähdä kaikki haun aikana käsitellyt solmut, koodi tätä varten löytyy dijkstra.py-tiedoston pohjalta. Koodin saa käyttöön poistamalla rivien eteen asetetut #-merkit.

	- Algoritmilla muodostetun polun voi pyyhkiä kartalta painamalla näppäimistön c-näppäintä.

2. Jump Point Search: Paina näppäimistöllä j-näppäintä. Kartalle piirtyy sinisistä ruuduista muodostuva optimaalisen mittainen polku lähtö- ja maaliruutujen välille. Komentoriville tulostuu tieto siitä, kuinka kauan reitinhaku kesti ja kuinka pitkä löydetty polku on. Jos haluat nähdä löydetyt hyppypisteet tai kaikki tutkitut ruudut kartalla, koodi tähän löytyy jps.py-tiedoston pohjalta. Koodin saa käyttöön poistamalla sen eteen asetetut #-merkit.


## Testit

- Ohjelman testit saa suoritettua komennolla *poetry run invoke test*
- Testikattavuuden saa tallennettua htmlcov-kansion index.html-tiedostoon komennolla *poetry run invoke coverage-report*


## Muut

- Ohjelman koodia sisältävien tiedostojen pylint-tarkistuksen tulokset saa näkyviin komennolla *poetry run invoke lint*
- Ohjelman koodia sisältävien tiedostojen formatoinnin saa tehtyä komennolla *poetry run invoke format*
