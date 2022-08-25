import unittest
from translator import english_to_french
from translator import french_to_english

text_in_english='Hello'
text_in_french='Bonjour'

class Test(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french(text_in_english),text_in_french)
    
    def test_english_to_french(self,**args):
        self.assertNotEqual(english_to_french(None),text_in_french)

    def test_french_to_english(self):
        self.assertEqual(french_to_english(text_in_french),text_in_english)

    def test_french_to_english(self,**args):
        self.assertNotEqual(french_to_english(None),text_in_english)

if __name__=='__main__':
    unittest.main()
