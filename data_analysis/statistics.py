from collections import Counter
from data_analysis import load


#statystyki słownika przy poleceniu --dictionary-stats - oddzielne funkcje
# funkcje przyjmują teksty

# liczba linii
def count_lines(text):
  return text.count("\n") + 1

def count_words(text):
  words = text.split()   # tu rozbijam tekst w formie str na listę słów
  number_of_words = len(words)
  unique_words = len(set(words))  # robię zbiór bo w zbiorze nie będzie powtórzeń
  return words, number_of_words, unique_words   # zwraca listę słów, liczbę słów i zbiór unikalnych słów

def top10_words(text):

  words=text.split()

  duplikaty = {}
  zliczenia = Counter(words)  # zwraca listę ze zliczeniami wyrazów

  for key, value in zliczenia.items():
      if value > 1:
          duplikaty[key] = value       # wrzucamy tylko te słowa, które wystepują częściej niż 1 raz

  posortowane = sorted(duplikaty.items(), key=lambda item: item[1], reverse=True)

  if len(posortowane) <= 10:
       return posortowane
  wynik_top10 = posortowane[:10]

  granica = wynik_top10[-1][1]

  for word, count in posortowane[10:]:
          if count == granica:
              wynik_top10.append((word, count))
          else:
            break

  return wynik_top10


def count_letters(text):
  words = text.split()
  licznik_liter = {}
  licznik_znakow = {}
  litery_polskie = "aąbcćdeęfghijklłmnoóprsśtuwyzźż"

  for word in words:

      for letter in word.lower():
          if letter in [" ", ",", "\n"]:
              pass
          if letter in litery_polskie:

              if letter in licznik_liter:
                  licznik_liter[letter] += 1
              else:
                  licznik_liter[letter] = 1

          else:
              if letter in licznik_znakow:
                  licznik_znakow[letter] += 1
              else:
                  licznik_znakow[letter] = 1

  #sortowanie licznika liter
  def sortujaca(item):
    literka = item[0]
    licznik = item[1]
    return (-licznik, litery_polskie.index(literka))

  licznik_liter_sorted = sorted(licznik_liter.items(), key=sortujaca)
  return licznik_liter_sorted, licznik_znakow


def stats(text):
  number_of_lines = count_lines(text)
  words, number_of_words, unique_words = count_words(text)

  wynik_top10 = top10_words(text)
  licznik_liter_sorted,licznik_znakow = count_letters(text)

  return (
          f'Number of lines: {number_of_lines}\n'
          f'Number of words: {number_of_words}\n'
          f'Number of unique words: {unique_words}\n'
          f'Top words with the most occurrences:{wynik_top10}\n'
          f'Letters with counters{licznik_liter_sorted}\n'
          f'Ohther characters:{licznik_znakow}\n'
          )

def dictionary_stats(path):
  text = load.load_dictionary_text(path)
  return stats(text)

def works_stats(file_names):  # argumentem będzie string z nazwą/nazwami plików, które trzeba odczytać

    texts, text_sum = load.load_works(file_names)
    lista = file_names.split(",")
    files = []
    for i in lista:
        cleaned = i.strip()
        files.append(cleaned)

    wynik = []
    wynik.append(f'Number of files:{len(files)}')

    if len(files) == 1:
        wynik.append(stats(texts[0]))
    else:
        for i, file in enumerate(files):
            wynik.append(f'\n{file}')
            wynik.append(stats(texts[i]))

        wynik.append("\nAll files")
        wynik.append(stats(text_sum))

    return "\n".join(wynik)