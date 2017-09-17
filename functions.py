import re
import requests
import json


# The function "count_words" get file with text, count the words and put them to dictionary,
# where key is a word and value is a tuple: count and translate


def count_words(file_name):
    dict_words = {}
    for string in open(file_name):
        words = (re.sub('\W', ' ', string.lower()).split())
        for word in words:
            if word in dict_words:
                dict_words[word][0] += 1
            else:
                param = [1,""]
                dict_words[word] = param
    return dict_words


# The function "translate_words" get dictionary from function count_words and Yandex translate
# token(for more information about it https://tech.yandex.ru/dictionary/), and translate the worlds
# use Yandex dictionary API. Update translate in a tuple.


def translate_words(dict_words, token):
    for word in dict_words:
        if len(word) > 3:
            link = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=' + token + '&lang=en-ru&text=' + word + '&flags=4'
            response = requests.get(link, timeout=10)
            translate = json.loads(response.text)
            try:
                word_tr = translate['def'][0]['tr'][0]['text']
            except IndexError:
                word_tr = "none"
            dict_words[word][1] = word_tr
    return dict_words


# The function "sort_words" sort by number descending


def sort_words(dict_words):
    dict_words = sorted(dict_words.items(), key=lambda x: x[1], reverse=True)
    return dict_words
