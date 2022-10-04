import unittest
from translator import english_to_french,french_to_english

class testMyModule(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french("I want to die"),"Je veux mourir")
        self.assertEqual(english_to_french(),"")
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(french_to_english("Je veux mourir"),"I want to die")
        self.assertEqual(french_to_english(),"")
unittest.main()
