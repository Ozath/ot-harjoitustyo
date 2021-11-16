import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassan_alku_arvot_oikein(self):
        # rahamaara on 1000 euroa ja myytja lounaita 0
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateis_edullinen_onnistunut_osto(self):
        # maksetaan kateisella 300 senttia joten..
        # kassassa on 100240 senttiä, edulliset laskuri kasvaa yhdellä,
        # maukkaat laskuri ei kasva, ja vaihtoraha on 60 senttiä
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_kateis_maukas_onnistunut_osto(self):
        # maksetaan kateisella 500 senttia joten..
        # kassassa on 100400 senttiä, maukkaat laskuri kasvaa yhdellä,
        # edulliset laskuri ei kasva, ja vaihtoraha on 100 senttiä
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_kateis_edullinen_ei_onnistunut_osto(self):
        # maksetaan kateisella 200 senttia joten..
        # kassassa on 100000 senttiä, edulliset laskuri ei kasva,
        # maukkaat laskuri ei kasva, ja vaihtoraha on 200 senttiä
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_kateis_maukas_ei_onnistunut_osto(self):
        # maksetaan kateisella 300 senttia joten..
        # kassassa on 100000 senttiä, edulliset laskuri ei kasva,
        # maukkaat laskuri ei kasva, ja vaihtoraha on 300 senttiä
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_kortilla_edullinen_onnistunut_osto(self):
        # kortilla 10 euroa joten..
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_kortilla_edullinen_ei_onnistunut_osto(self):
        # kortilla 2 euroa joten..
        self.maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_kortilla_maukas_onnistunut_osto(self):
        # kortilla 10 euroa joten..
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_kortilla_maukas_ei_onnistunut_osto(self):
        # kortilla 3 euroa joten..
        self.maksukortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(str(self.maksukortti), "saldo: 3.0")
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_kortille_onnistunut_rahan_lataus(self):
        # lataa kortille 1000 senttiä
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")

    def test_kortille_ei_onnistunut_rahan_lataus(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

