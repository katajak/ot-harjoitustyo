import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1" )

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.1")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.lataa_rahaa(990)
        self.maksukortti.ota_rahaa(400)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")

    def test_saldo_ei_muutu_jos_ei_ole_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(240)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_ota_rahaa_palauttaa_true_jos_rahaa_riittävästi(self):
        self.maksukortti.lataa_rahaa(990)
        self.assertEqual(self.maksukortti.ota_rahaa(240), True)

    def test_ota_rahaa_palauttaa_false_jos_rahaa_ei_ole_riittävästi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(240), False)