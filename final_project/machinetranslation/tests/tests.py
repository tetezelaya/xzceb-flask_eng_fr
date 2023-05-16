import unittest
from translator import english_to_french, french_to_english

class TestTranslationMethods(unittest.TestCase):

    def test_null_input_english_to_french(self):
        with self.assertRaises(TypeError):
            english_to_french(None)

    def test_null_input_french_to_english(self):
        with self.assertRaises(TypeError):
            french_to_english(None)

    def test_translation_hello(self):
        self.assertIn('Bonjour', english_to_french('Hello'))

    def test_translation_bonjour(self):
        self.assertIn('Hello', french_to_english('Bonjour'))

if __name__ == '__main__':
    unittest.main()
