import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassa_luodaan_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0) 

    def test_kateisosto_edullinen_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(280),40)
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa,100720)
        self.assertEqual(self.kassapaate.edulliset, 3)

    def test_kateisosto_ei_toimi_edullisesti_kun_liian_vahan_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(60),60)
        self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_kateisosto_maukas_toimii(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(440),40)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa,101200)
        self.assertEqual(self.kassapaate.maukkaat, 3)

    def test_kateisosto_ei_toimi_maukkaasti_kun_liian_vahan_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(60),60)
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_kortilla_ostaminen_edullinen_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),True)
        self.assertEqual(self.maksukortti.saldo,760)
        self.assertEqual(self.kassapaate.edulliset,1)
    
    def test_kortilla_ostaminen_edullinen_ei_toimi_ilman_rahaa(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti),False)
        self.assertEqual(kortti.saldo,100)
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_kortilla_ostaminen_maukas_toimii(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),True)
        self.assertEqual(self.maksukortti.saldo,600)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_kortilla_ostaminen_maukas_ei_toimi_ilman_rahaa(self):
        kortti = Maksukortti(300)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti),False)
        self.assertEqual(kortti.saldo,300)
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_kortille_rahan_lataaminen_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,300)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1003)
        self.assertEqual(self.maksukortti.saldo,1300)

    def test_kortille_laataaminen_negatiivinen_arvo_ei_toimi(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-300)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000)
        self.assertEqual(self.maksukortti.saldo,1000)