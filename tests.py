import unittest
from dictionary_tool import get_word_definition

class DictionaryToolTests(unittest.TestCase):

    def test_get_word_definition(self):
        word = "exercise"
        pronunciation, word_type, definition = get_word_definition(word)
        self.assertEqual(pronunciation, "ˈek-sər-ˌsīz")
        self.assertEqual(word_type, "noun")
        self.assertEqual(definition, "the act of bringing into play or realizing in action")

    def test_get_word_definition_not_found(self):
        word = "nonexistentword"
        result = get_word_definition(word)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
