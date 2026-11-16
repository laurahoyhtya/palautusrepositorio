# Reflektio

Agentti siirsi yhteiset mockien ja kaupan alustukset `setUp`-metodiin, mikä vähensi toistoa järkevästi. Testien ostotilanteet ja odotetut maksutiedot erottuvat nyt paremmin, joten koodi on mielestäni helpompi lukea.

`setUp`-muutos ei poistanut eikä heikentänyt tarkistuksia: testeissä tarkistetaan edelleen `assert_called_once_with`-metodilla, että pankkia kutsutaan täsmälleen kerran oikeilla tiedoilla. Jo aiemmassa muutoksessa alkuperäinen yleinen `assert_called`-tarkistus oli korvattu neljällä tarkemmalla testillä.

Pyysin agenttia erikseen siirtämään yhteiset alustukset `setUp`-metodiin. En tehnyt muutoksia itse; tarkistin lopuksi, että kaikki neljä testiä menivät läpi.
