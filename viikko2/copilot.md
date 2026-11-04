# Kokemuksia Copilotista

Käytin Copilotin ehdotuksia apuna `nhl-reader`-projektissa. Koodin täydennykset olivat hyödyllisiä erityisesti toistuvassa rakenteessa, kuten pelaajatietojen käsittelyssä ja testien rungossa. Ehdotuksia piti silti lukea ja verrata tehtävän vaatimuksiin ennen niiden hyväksymistä.

Pylint-varoituksen selitys piti paikkansa, kun kyse oli `too-few-public-methods`-säännöstä. Se huomauttaa luokasta, jolla on vain vähän julkisia metodeja; kyseessä on rakenteeseen liittyvä laatuhuomautus, ei automaattisesti toiminnallinen virhe. Esimerkiksi dataa kuvaavalla `Player`-luokalla tai pelaajat lukevalla luokalla on luontevasti vain vähän metodeja, joten varoituksen voi perustellusti ohittaa, kun sen syyn ymmärtää.

Agentti teki toimivan ratkaisun ja yksikkötestit. Testeissä käytetään `PlayerReaderStub`-luokkaa oikean lukijan sijaan, joten testit eivät tarvitse verkkoyhteyttä. Ajoin testit komennolla `uv run --group dev pytest`; kaikki viisi testiä menivät läpi.

Testien perusratkaisu ei eronnut olennaisesti edellisestä viikosta: molempien viikkojen testit käyttävät `unittest.TestCase`-luokkaa ja riippuvuuden tilalla testistubia. Tällä viikolla testit ajettiin kuitenkin pytestillä, ja ne kattavat kansalaisuuden ja joukkueen mukaan suodatusta sekä järjestämistä ja tulosmäärän rajaamista.

Lopullisessa koodissa Pylint ei löytänyt virheitä: `uv run --group dev pylint src` antoi tulokseksi 10/10. Tämä muistutti siitä, että agentin tuottama koodi kannattaa tarkistaa sekä testeillä että staattisella analyysillä.

Opin myös, että agentilta saa paremmin käyttökelpoisia tuloksia, kun tehtävänannon ehdot kertoo täsmällisesti. Tässä testeissä tärkeä ehto oli verkkoyhteyden välttäminen. Lisäksi Pylintin huomautuksia kannattaa tulkita niiden tarkoituksen kautta: kaikki varoitukset eivät merkitse ohjelman rikkoutumista, mutta ohitus pitää pystyä perustelemaan.
