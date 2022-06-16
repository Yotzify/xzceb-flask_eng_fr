import unittest

from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        self.assertEqual(englishToFrench('Car'),'Voiture')

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(frenchToEnglish('Voiture'),'Car')

unittest.main() 