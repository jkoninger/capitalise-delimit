import unittest
from capitalise_delimit import CapitaliseDelimit


class CapitaliseDelimitTestCase(unittest.TestCase):

    def setUp(self):
        self.string = CapitaliseDelimit('some-sequence of@random~words')

    def test_single_word_no_delimiters(self):
        self.assertEqual(CapitaliseDelimit('string').capitalise([]), 'String')

    def test_multiple_words_no_delimiters(self):
        self.assertEqual(self.string.capitalise([]), 'Some-sequence of@random~words')

    def test_empty_string_no_delimiters(self):
        self.assertEqual(CapitaliseDelimit('').capitalise([]), '')

    def test_empty_string_with_delimiters(self):
        self.assertEqual(CapitaliseDelimit('').capitalise([' ', '@']), '')

    def test_single_word_with_delimiters(self):
        self.assertEqual(CapitaliseDelimit('string').capitalise(['-', ' ', '@', '~']), 'String')

    def test_multiple_words_with_some_delimiters(self):
        self.assertEqual(self.string.capitalise(['-', '@']), 'Some-Sequence of@Random~words')

    def test_multiple_words_with_all_relevant_delimiters(self):
        self.assertEqual(self.string.capitalise(['-', ' ', '@', '~']), 'Some-Sequence Of@Random~Words')

    def test_multiple_words_with_extra_delimiters(self):
        self.assertEqual(self.string.capitalise(['-', ' ', '@', '~', '?', '/']), 'Some-Sequence Of@Random~Words')


if __name__ == '__main__':
    unittest.main()
