def prepare_text(text):

  text = text.lower()
  for character in [".",",","!","?",":",";","„","”","—","–","…",")","(","/"]:
            text = text.replace(character, " ")
  return text

def load_dictionary(path):
    dictionary = {}

    with open(path, encoding="utf-8") as f:
        for line in f:
            words = line.strip().split(", ")
            base_word = words[0]
            dictionary[base_word] = words
    return dictionary


def load_dictionary_text(path):  # do funkcji statystyk - zwraca tekst - słowa słownika i tekstów bez zbędnych znaków
    with open(path, encoding="utf-8") as f:
        return prepare_text(f.read())


def load_works(paths):
    texts = []
    text_sum = ""
    for file in paths.split(","):
      file=file.strip()  # usuwa spacje w razie czego
      with open(file, encoding="utf-8") as f:

          text = prepare_text(f.read())
          texts.append(text)  # lista z osobnymi str odpowiadającymi każdemu tekstowi
          text_sum += text + "\n" # napis z sumą wszystkich słów z wszystkich tekstów

    return texts, text_sum