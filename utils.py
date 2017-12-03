import re
import json

import operator

data = json.load(open('words_dictionary.json'))


def word_exists(word):
    return word in data


def init_frequency_dictionary(result):
    for val in range(ord('z') - ord('a') + 1):
        result[chr(ord('a') + val)] = 0


def print_frequencies(result):
    for key, value in result:
        print key, " : ", value


def append_frequencies_for_word(word, result):
    for letter in word:
        if letter.isalpha():
            result[letter] = result[letter] + 1


def get_frequencies(words=data, descriptor="data"):
    result = {}
    init_frequency_dictionary(result)
    print "Analyzing ", descriptor, " frequency..."
    for word in words:
        append_frequencies_for_word(word, result)
    result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)

    print_frequencies(result)
    print "Done."

    return result


def read_input_sentence():
    with open('input.txt', 'r') as content_file:
        return content_file.read().lower()


def get_words(sentence):
    return re.sub("[^\w]", " ", sentence).split()


def get_sentence_percentage(sentence):
    wordList = get_words(sentence)
    matches = 0
    for word in wordList:
        if word_exists(word):
            matches += 1

    return matches * 100 / len(wordList)


def get_shifted_char(c, shift):
    new_position = ord(c) + shift
    if new_position > ord('z'):
        new_position = ord('a') + new_position - ord('z') - 1
    if new_position < ord('a'):
        new_position = ord('z') - (ord('a') - new_position) + 1
    return chr(new_position)
