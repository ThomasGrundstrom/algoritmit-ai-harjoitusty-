# Toteutusdokumentti

Kuten määrittelydokumentissa mainittiin, projektia varten on toteutettu JPS-algoritmi ja Dijkstran algoritmi etsimään lyhimpiä reittejä kaksiulotteisella "kartalla". Kartta on toteutettu taulukkona, joka sisältää numeroita. Numerot vastaavat seuraavia asioita: 
- 0: Tyhjä ruutu, eli ruutu, jonka läpi voi kulkea. Harmaita ruutuja pygame displayn kartalla.
- 1: Lähtöruutu, eli piste, josta reitinhaku lähtee käyntiin. Vihreä ruutu pygame-displayn kartalla.
- 2: Maaliruutu, eli ruutu, johon reitinhaku päättyy. Punainen ruutu pygame-displayn kartalla.
- 3: Seinä-, tai esteruutu. Reitti ei saa kulkea näiden ruutujen läpi. Musta ruutu pygame-displayn kartalla.
- 4: Ruutu, joka on osa optimaalista polkua. Näitä ruutuja ei ole aluksi kartalla ollenkaan, mutta reitinhakualgoritmin suorittamisen jälkeen optimaalisella polulla olevat arvot kartalla muuttuvat luvuksi 4. Sininen ruutu pygame-displayn kartalla.
- 5: Ruutu, joka on tutkittu reitinhaun aikana, tai ruutu, jonka JPS luokittelee hyppypisteeksi. Näitä ruutuja ei tule kartalle näkyviin, ellei niiden näyttämistä varten tehdyn koodin edestä ei ole poistettu #-merkkejä dijkstra.py- ja jps.py-tiedostoista.


## Dijkstran algoritmi

- Algoritmia voi kutsua painamalla näppäimistön d-näppäintä.
Dijkstran algoritmi käyttää apunaan verkkoa, joka luodaan vastaamaan annettua karttaa algoritmin kutsumisvaiheessa. Verkko koostuu solmuista ja niitä yhdistävistä kaarista, joilla on tietyt pituudet. Jokaisesta solmusta kulkee kaari jokaiseen välittömään naapuriin. Näistä kaarista suoraan (ylös, alas, vasen, oikea) kulkevien kaarten pituus on 1, ja diagonaalisesti kulkevien kaarten pituus on sqrt(2). Algoritmi siirtää tutkittavan ruudun naapurit pinoon, josta poimii naapureita tutkittavaksi siten, että pienemmän etäisyyden naapurit tutkitaan ensin ja kauempana olevat niiden jälkeen. Siirryttäessä seuraavaan solmuun, uuden solmun "self.edellinen"-arvo asetetaan viittaamaan aiemmin tutkittuun solmuun. Kun saavutetaan maalisolmu, voidaan piirtää polku alun ja maalin välille siirtyen loppusolmusta aiempaan solmuun siihen asti, kunnes aiempi solmu on alkusolmu.


## JPS-algoritmi

- Algoritmia voi kutsua painamalla näppäimistön j-näppäintä.
JPS-algoritmin ideana on, että optimaalinen reitti voidaan löytää käyttäen vain "hyppypisteitä" ja jättämällä väliin näiiden välillä olevien ruutujen laajempi tutkiminen. Algoritmi kulkee verkossa kahdeksaan suuntaan ja löydettyään "hyppypisteen", eli kandidaatin pisteelle, jonka läpi optimaalinen polku voisi kulkea, jatkaa etsimistä hyppypisteen kohdalta. Löydettyjen hyppypisteiden tutkimisjärjestys määrittyy sen mukaan, millä niistä on pienin oletusarvo lopullisen reitin pituudesta, kun reitti kulkee hyppypisteen kautta. Tämä on toteutettu jps.py-tiedostosta löytyvällä Priorityqueue-luokalla. Kuten Dijkstran algoritmissa, myös Jump Point Search:ssa solmuihin talletetaan niiden edeltäjät ja niiden avulla voidaan lopuksi piirtää optimaalinen polku lähtö- ja maalipisteiden välillä.


### Kielimallit

En ole käyttänyt ChatGPT:tä tai muita kielimalleja kurssilla.
