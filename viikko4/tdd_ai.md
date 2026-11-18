# Kokemuksia TDD-työskentelystä agentin kanssa

## Toteutuksen ja testien laatu

Lopputulos vastaa testien kuvaamaa ostoskorin toimintaa. Ostoslista on nyt korin ainoa tallennettu tila: tavaramäärä ja hinta lasketaan sen alkioista. Tämä vähentää mahdollisuutta, että ostoslista ja erilliset laskurit ajautuisivat eri tilaan. Testit kattavat tuotteen lisäämisen, saman tuotteen yhdistämisen ostokseksi, poistamisen ja korin tyhjentämisen. Testit ovat selkeitä, vaikka tuotteiden luonti ja lisääminen toistuvat useissa testeissä.


## Osa A: minimitoteutus ja testit

Kun tehtävänä oli muuttaa toteutusta, testit jätettiin yleensä rauhaan. Testeihin tehtiin muutoksia silloin, kun tehtävänä oli nimenomaan uuden testin kirjoittaminen. Refaktorointi vaiheessa ostoslistan kopion palauttamiseen lisättiin myös suoraan sitä varmistava testi, mutta mielestäni tämä on ihan hyvä asia.

Minimitoteutus ei aina tarkoittanut, että jokainen myöhempi testi olisi ensin epäonnistunut. Esimerkiksi tuotteen lisäyksen hinta- ja tavaramäärälogiikka sai myöhemmät usean tuotteen testit menemään läpi heti. Tämä johtui siitä, että toteutus käsitteli lisäyksiä yleisesti eikä vain yhtä testitapausta. Aluksi `tavaroita_korissa()` palautti vakiona nollan, mikä riitti vain tyhjän korin testiin; lisäystestin jälkeen se vaihdettiin tilaa seuraavaan toteutukseen.

## Testien odotusarvojen kovakoodaus

Agentti ei yrittänyt tarkoituksella huijata testejä tai sovittaa toteutusta testien nimiin. Testien odotettuja tuloksia ei kovakoodattu.

## Työnjako A vai B

B tuntui tehokkaammalta: agentti kirjoitti testin annetun vaatimuksen pohjalta, testi ajettiin, ja epäonnistumisen jälkeen toteutus korjattiin. Itse testin kirjoittaminen tuntui huomattavasti työläämmältä, vaikka se toki toimi hyvänä harjoituksena. 
