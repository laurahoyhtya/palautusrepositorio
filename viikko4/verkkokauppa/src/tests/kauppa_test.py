import unittest
from unittest.mock import Mock
from kauppa import Kauppa
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def _suorita_ostos(self, tuotteet, saldot, tuote_idt):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 42
        varasto_mock = Mock()
        varasto_mock.saldo.side_effect = lambda tuote_id: saldot[tuote_id]
        varasto_mock.hae_tuote.side_effect = lambda tuote_id: tuotteet[tuote_id]

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        for tuote_id in tuote_idt:
            kauppa.lisaa_koriin(tuote_id)
        kauppa.tilimaksu("pekka", "12345")

        return pankki_mock

    def test_maksettaessa_yksi_ostos_tilisiirto_kutsutaan_oikeilla_tiedoilla(self):
        tuotteet = {1: Tuote(1, "maito", 5)}
        pankki_mock = self._suorita_ostos(tuotteet, {1: 10}, [1])

        pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_maksettaessa_kaksi_eri_tuotetta_hinnat_lasketaan_yhteen(self):
        tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "leipa", 3),
        }
        pankki_mock = self._suorita_ostos(tuotteet, {1: 10, 2: 5}, [1, 2])

        pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 8
        )

    def test_maksettaessa_kaksi_samaa_tuotetta_hinta_lasketaan_molemmille(self):
        tuotteet = {1: Tuote(1, "maito", 5)}
        pankki_mock = self._suorita_ostos(tuotteet, {1: 10}, [1, 1])

        pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 10
        )

    def test_loppunut_tuote_ei_korota_maksettavaa_summaa(self):
        tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "leipa", 3),
        }
        pankki_mock = self._suorita_ostos(tuotteet, {1: 10, 2: 0}, [1, 2])

        pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 5
        )
