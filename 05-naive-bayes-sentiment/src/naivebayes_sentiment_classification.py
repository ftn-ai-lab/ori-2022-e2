import re
import string
import math
import pandas as pd


def load_data():
    # TODO 1: ucitati podatke iz data/train.tsv datoteke
    # rezultat treba da budu dve liste, texts i sentiments
    raise NotImplementedError('TODO 1')
    texts, sentiments = [], []
    return texts, sentiments


def preprocess(text):
    # TODO 2: implementirati preprocesiranje teksta
    # - izbacivanje znakova interpunkcije
    # - svodjenje celog teksta na mala slova
    # rezultat treba da bude preprocesiran tekst
    raise NotImplementedError('TODO 2')
    return text


def tokenize(text):
    text = preprocess(text)
    # TODO 3: implementirati tokenizaciju teksta na reci
    # rezultat treba da bude lista reci koje se nalaze u datom tekstu
    raise NotImplementedError('TODO 3')
    words = []
    return words


def count_words(text):
    words = tokenize(text)
    # TODO 4: implementirati prebrojavanje reci u datum tekstu
    # rezultat treba da bude mapa, ciji kljucevi su reci, a vrednosti broj ponavljanja te reci u datoj recenici
    raise NotImplementedError('TODO 4')
    words_count = {}
    return words_count


def fit(texts, sentiments):
    # inicijalizacija struktura
    bag_of_words = {}               # bag-of-words za sve recenzije
    words_count = {'pos': {},       # isto bag-of-words, ali posebno za pozivitne i negativne recenzije
                   'neg': {}}
    texts_count = {'pos': 0.0,      # broj tekstova za pozivitne i negativne recenzije
                   'neg': 0.0}

    # TODO 5: proci kroz sve recenzije i sentimente i napuniti gore inicijalizovane strukture
    # bag-of-words je mapa svih reci i broja njihovih ponavljanja u celom korpusu recenzija
    raise NotImplementedError('TODO 5')
    return bag_of_words, words_count, texts_count


def predict(text, bag_of_words, words_count, texts_count):
    words = tokenize(text)          # tokenizacija teksta

    # TODO 6: implementirati Naivni Bayes klasifikator za sentiment teksta (recenzije)
    # rezultat treba da bude mapa verovatnoca da je dati tekst klasifikovan kao pozitivnu i negativna recenzija
    raise NotImplementedError('TODO 6')
    score_pos, score_neg = 0.0, 0.0
    return {'pos': score_pos, 'neg': score_neg}

if __name__ == '__main__':
    # ucitavanje data seta
    texts, sentiments = load_data()

    # izracunavanje / prebrojavanje stvari potrebnih za primenu Naivnog Bayesa
    bag_of_words, words_count, texts_count = fit(texts, sentiments)

    # recenzija
    text = 'I really liked this movie.'

    # klasifikovati sentiment recenzije koriscenjem Naivnog Bayes klasifikatora
    predictions = predict(text, bag_of_words, words_count, texts_count)

    print('-'*30)
    print('Review: {0}'.format(text))
    print('Score(pos): {0}'.format(predictions['pos']))
    print('Score(neg): {0}'.format(predictions['neg']))
