import pandas as pd
from collections import Counter
from data_analysis import load
import os
from data_analysis import statistics



def frequencies(text, n):

      words = text.split()

      counter = Counter(words)

      most_common = counter.most_common()  # zwraca listę krotek

      if len(most_common) <= n:
          return most_common

      nth_word = most_common[n - 1]
      cutoff = nth_word[1]

      result = []

      for item in most_common:
          if item[1] >= cutoff:
              result.append(item)

      return result

def files_frequencies(files,texts,n):

    lista = []
    for file in files.split(","):
        lista.append(file.strip())

    wynik = []

    for i in range(len(texts)):
        wynik.append(lista[i])
        wynik.append(str(frequencies(texts[i],n)))

    return "\n".join(wynik)


def no_words(dictionary_file, work_files):
    dictionary_text = load.load_dictionary_text(dictionary_file)
    dictionary_words = set(dictionary_text.split())  # zbiór słów ze słownika bez powtórzeń

    texts, text_sum = load.load_works(work_files) # dostęp do tekstów i sumy wszystkich tekstów

    work_words,number_of_words, unique_words= statistics.count_words(text_sum)  # pierwsza wartość funkcji count_words to lista słów z sumy tekstów

    policzone = Counter(work_words)     # zlicza które słowo występuje ile razy - ma strukturę słownika word: count

    brakujace = {}               # tworzę słownik - słowa brakujące wraz ze zliczeniami

    for word, count in policzone.items():
        if word not in dictionary_words:
            brakujace[word] = count    # dodaję słowa, których nie ma w słowniku wraz ze zliczeniami
    output_text = ""

    for word, count in brakujace.items():
        output_text += f"{word}: {count}\n"


    return output_text

def similarity(tekst1, tekst2, n,print_results = False):

    slowa1 = tekst1.split()
    slowa2 = tekst2.split()
    licznik1 = Counter(slowa1)  # policzy słowa jeżeli w argumencie będzie lista słów
    licznik2 = Counter(slowa2)


    top1 = licznik1.most_common(n)
    top2 = licznik2.most_common(n)


    slowa1_top = []

    for word, count in top1:
        slowa1_top.append(word)

    slowa2_top = []

    for word, count in top2:
        slowa2_top.append(word)

    wspolne = 0
    wspolne_slowa = []

    for word in slowa1_top:
        if word in slowa2_top:
            wspolne += 1
            wspolne_slowa.append(word)

    all_words = []

    for word in slowa1_top:
        if word not in all_words:     
            all_words.append(word)

    for word in slowa2_top:
        if word not in all_words:
            all_words.append(word)
    if print_results:
        print(f'Liczba wspólnych:{wspolne}')
        print(f'Lista wspolnych: {wspolne_slowa}')
        print(f'Liczba całość:{len(all_words)}')
        print(f'Lista całość:{all_words}')


    similarity = wspolne / len(all_words) * 100


    return round(similarity)


def similarity_comparison(files,texts,n,output_path):
  titles = []

  for i in files.split(","):
    titles.append(i.strip())
  df_wyniki = []
  wyniki_output = []
  for k in range(len(texts)):
      for j in range(k+1,len(texts)):
          if k!=j:
            print("===============")
            wynik_similarity = similarity(texts[k], texts[j], n, True)
            print(f'Tekst {k} vs. tekst {j}: wynik similarity: {wynik_similarity}')

            df_wyniki.append({"File 1": titles[k],
                "File 2": titles[j],
                "Similarity": wynik_similarity})

            wyniki_output.append(f'{titles[k]} vs {titles[j]} --> {wynik_similarity}\n ')

  os.makedirs(output_path, exist_ok=True)
  path = os.path.join(output_path, "similarity_results.csv")
  df = pd.DataFrame(df_wyniki)
  df.to_csv(
      path,
      index=False,
      encoding="utf-8"
  )
  #print(df)
  return "\n".join(wyniki_output)
