import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alku_saldo_oikein(self):
        # alkusaldo on 1000 senttiä eli 10 euroa
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_testaa_lataus_toimii_oikein(self):
        # lisää 100 senttiä eli 1 euro, joten loppu saldo on 11 euroa
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 11.0")

    def test_rahan_otto_onnistuu_jos_saldoa(self):
        # yritä ottaa 5 euroa, eli 500 senttiä
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")

    def test_rahan_otto_ei_onnistu_jos_ei_saldoa(self):
        # yritä ottaa 15 euroa, eli 1500 senttiä
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_otto_palauttaa_true_jos_saldoa(self):
        # yritä ottaa 5 euroa, eli 500 senttiä palauttaa true
        self.assertTrue(self.maksukortti.ota_rahaa(500))

    def test_rahan_otto_palauttaa_false_jos_ei_saldoa(self):
        # yritä ottaa 15 euroa, eli 1500 senttiä palauttaa false
        self.assertFalse(self.maksukortti.ota_rahaa(1500))
