# Katselmoinnin raportti

## Mitä huomioita Copilot teki koodista

GitHub Copilot teki pull request -katselmoinnissa huomion
`won_point`-metodin muuttuneesta kutsurajapinnasta. Ensin
`won_point` vertasi pisteen antajaa
`"player1"`/`"player2"`-roolitunnisteiden sijasta konstruktorin
näyttönimiin. Tämä muuttaisi aiemman toiminnan: metodin olemassa
olevissa kutsuissa annetaan roolitunniste `"player1"` tai
`"player2"`, vaikka konstruktorille voisi antaa myös toiset nimet,
esimerkiksi `"Alice"` ja `"Bob"`.

Copilot ehdotti, että attribuointi säilytetään roolitunnisteiden
pohjalta tai että koko API ja kaikki kutsukohdat päivitetään
yhdenmukaisesti näyttönimiä käyttäväksi.

## Olivatko ehdotetut muutokset hyviä

Ehdotus oli hyvä ja korjauksen kannalta riittävä. Koska
`src/index.py` ja testit käyttävät jo roolitunnisteita, olisi
huono muuttaa vain `won_point`-metodia näyttönimien mukaiseksi:
piste voisi tällöin päätyä väärälle pelaajalle. Pienin ja
yhteensopivin muutos on pitää `won_point("player1")` ja
`won_point("player2")`-kutsut ennallaan.

Näyttönimiä voidaan samalla edelleen käyttää tulostuksissa. Tämän
kautta rajapinta ei muutu eikä testeihin tarvitse koskea.

## Copilotin katselmoinnin hyödyn arvio

Katselmointi oli hyvin hyödyllinen. Se löysi konkreettisen
taannehtivan ongelman, joka ei välttämättä näkyisi alkuperäisten
testien läpi ajossa, jos testit käyttävät aina tunnisteita
`"player1"` ja `"player2"` näyttöniminä.

Kommentti oli myös käyttökelpoinen, koska se käytti todennettavia
esimerkkejä olemassa olevista kutsukohdista. Se helpotti päätöstä
siitä, mitä muutosta ei pidä tehdä.

## Mitä Copilot huomasi ja mitä se saattoi jättää huomaamatta

Copilot huomasi itse näiden näyttönimien ja roolitunnisteiden väisen
ristiriidan, jonka olisi helppo jättää huomaamatta refaktorointia
tehdessä. Koodissa olevat nimet ovat samankaltaisia, mutta niillä
on eri tehtävä: `player1_name` on nimi tulostukseen, kun taas
`won_point`-metodin parametrin arvot ovat kutsukohdissa rooleja.

Kommentin perusteella ei voida kuitenkaan päätellä, että
Copilot olisi suorittanut kattavan katselmoinnin kaikista
refaktoroinnin mahdollisista ongelmista. Katselmointi on
siksi hyvä lisä ihmisen katselmoinnille, ei sen korvike.

## Vertailu ihmiskatselmoijaan

Copilotin kommentti muistutti tiimikaverin terävästi kohdennettuja
palautteita: se viittasi tiettyyn koodiriviin ja selitti käytännön
vaikutuksen. Ihmiskaveri voisi kuitenkin antaa enemmän taustaa,
kysyä API:n odotettua merkitystä, ehdottaa toista ratkaisua ja
huomioida projektin muiden osien sopimukset.

Ihmisen kanssa on tärkeää kertoa havaittu ongelma ensin
konkreettisella esimerkillä ja perustella, miksi se on ongelma.
Palautteen antajan kannattaa ehdottaa yhtä tai useampaa
toteutustapaa, mutta ei luokitella kaikkia muutosehdotuksia yhtä
kriittisiksi. Pakollinen korjaus kannattaa erottaa
laatuparannuksesta, ja palaute on hyvä antaa kunnioittavasti,
suoraan ja aloittelijaystävällisesti. Lopuksi tulisi tarkistaa,
että muutos säilyttää ohjelman olemassa olevan käyttäytymisen.

Copilot on nopea ja toimittaa teknisesti tarkkaa palautetta, mutta
ihmiskatselmoija ymmärtää helpommin koko projektin suunnitelmia,
ryhmän sopimuksia ja refaktoroinnin tarkoitusta.
