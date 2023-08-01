import unittest
from mydictionary import get_word_definition

class DictionaryToolTests(unittest.TestCase):

    def test_get_word_definition(self):
        word = "exercise"
        pronunciation, word_type, definition = get_word_definition(word)
        self.assertEqual(pronunciation, "ex*er*cise") 
        self.assertEqual(word_type, "noun")
        self.assertEqual(definition, "the act of bringing into play or realizing in action : use")


if __name__ == '__main__':
    unittest.main()
