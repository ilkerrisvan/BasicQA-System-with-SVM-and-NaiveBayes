from snowballstemmer import TurkishStemmer
import nltk

def run():
    turkStem=TurkishStemmer()
    input_data = input("Lütfen sorunuzu girin.")

    words = nltk.word_tokenize(input_data)
    words = [word.lower() for word in words if word.isalpha()]
    after_stem = [turkStem.stemWord(word) for word in words]
    print("AFTER SNOWBALL STEMMER: ", after_stem)

    ##print(after_stem)
    ## print("after stem",turkStem.stemWord(a))
    ## print(turkStem.stemWord("ilişkilendiremediklerimiz, selam, gözlük , gözlem"))

    return after_stem

def run_for_svm():
    turkStem=TurkishStemmer()
    input_data = input("Lütfen sorunuzu girin.")

    words = nltk.word_tokenize(input_data)
    sentence = ""
    after_stem = [turkStem.stemWord(word) for word in words]
    for i in range(len(after_stem)):
        sentence += after_stem[i]
        sentence += " "

    print("AFTER SNOWBALL STEMMER: ", after_stem)

    ##print(after_stem)
    ## print("after stem",turkStem.stemWord(a))
    ## print(turkStem.stemWord("ilişkilendiremediklerimiz, selam, gözlük , gözlem"))

    return sentence


