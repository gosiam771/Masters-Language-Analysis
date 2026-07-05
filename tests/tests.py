import unittest

from data_analysis import load
from data_analysis import analysis
from data_analysis import statistics


class TestPrepareText(unittest.TestCase):

  def test_prepare_short_text(self):
      text = "Funkcja, która testuje."
      result = load.prepare_text(text)
      self.assertEqual(result,"funkcja  która testuje ")


# dla count_words()
class TestCountWords(unittest.TestCase):

    def test_words_(self):
        test_text = "funkcja  która testuje testuje "
        words, number_of_words, unique_words = statistics.count_words(test_text)

        self.assertEqual(words, ["funkcja", "która", "testuje", "testuje"])

    def test_number_of_words_(self):
        test_text = "funkcja  która testuje testuje "
        words, number_of_words, unique_words = statistics.count_words(test_text)

        self.assertEqual(number_of_words, 4)

    def test_unique_words_(self):
        test_text = "funkcja  która testuje testuje "
        words, number_of_words, unique_words = statistics.count_words(test_text)

        self.assertEqual(unique_words, 3)


# dla count_lines()
class TestCountLines(unittest.TestCase):

    def test_count_lines(self):
        text = "funkcja która testuje\nfunkcja która testuje\nfunkcja która testuje"
        result = statistics.count_lines(text)
        self.assertEqual(result, 3)

# dla top10_words()
class TestTop10Words(unittest.TestCase):
  def test_top10_words(self):
    test_text = 'a a b b b c c c d d d d e e e e f f f f f g  h h i  i i i j j k k k'
    result = statistics.top10_words(test_text)
    self.assertEqual(result, [('f', 5), ('d', 4), ('e', 4), ('i', 4), ('b', 3), ('c', 3), ('k', 3), ('a', 2), ('h', 2), ('j', 2)])

# dla load_dictionary()
class TestLoadDictionary(unittest.TestCase):
  def test_load_dictionary(self):
    result = load.load_dictionary(r"C:\Users\Admin\PycharmProjects\PythonProject4test\tests\test_dictionary.txt")
    self.assertEqual(result,{'Abel': ['Abel', 'Abla', 'Ablem', 'Ablowi', 'Ablu']})

# dla similarity()
class TestSimilarity(unittest.TestCase):

  def test_similarity(self):
    tekst1= "ala ala ala ma ma kota psa i rybki rybki"
    tekst2 = "ala ala ala ma ma ma psa psa psa psa chomika oraz oraz papugę"
    result = analysis.similarity(tekst1,tekst2,3)
    self.assertEqual(result,50)

if __name__ == '__main__':
    unittest.main()
