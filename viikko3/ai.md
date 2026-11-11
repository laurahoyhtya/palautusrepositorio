# Kokemuksia AI-agentin käytöstä

Agentti generoi ohjetiedoston, joka oli aluksi liian pitkä eikä sisältänyt
kaikkia työn kannalta olennaisia asioita. Jouduin korjaamaan ohjetta
tiivistämällä sitä ja täydentämällä puuttuvia kohtia.

Agentti noudatti pyyntöä kirjoittaa testit ennen toteutusta. Minun tarvitsi
ohjata agenttia matkan varrella melko vähän.

Rikoin toteutuksen tarkoituksella kahdella tavalla: sallin pelkistä kirjaimista koostuvan salasanan ja poistin salasanan vahvistuksen tarkistuksen. Molempien muutosten jälkeen niitä vastaavat testit hajosivat, joten testit tunnistivat virheellisen toiminnan.

Opin, että tarkoituksella tehtyjen virheiden avulla voi arvioida testien
hyödyllisyyttä: testien läpäiseminen ei yksin riitä, vaan niiden pitää myös
epäonnistua, kun vaadittu toiminta rikkoutuu.
