import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_luotu_kortti_oikea_saldo(self):
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 10.00 euroa')

    def test_lataaminen_toimii_oikin(self):
        self.maksukortti.lataa_rahaa(400)

        self.assertEqual(self.maksukortti.saldo_euroina(),14.0)

    def test_ottaminen_toimii_oikein(self):
        self.maksukortti.ota_rahaa(200)

        self.assertEqual(self.maksukortti.saldo_euroina(),8.0)

    def test_ottaminen_liikaa_ei_muuta_saldoa(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(self.maksukortti.saldo_euroina(),10.0)

    def test_ota_rahaa_metodi_palauttaa_true_kun_rahaa_otetaan_oikein(self):

        self.assertEqual(self.maksukortti.ota_rahaa(200),True)

    def test_ota_rahaa_metodi_palauttaa_false_kun_rahaa_otetaan_vaarin(self):

        self.assertEqual(self.maksukortti.ota_rahaa(2000),False)