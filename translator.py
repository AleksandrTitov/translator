import re
import requests
import json

token = "YOU YANDEX TRANSLATE TOKEN"
file = "FILE WITH ENGLISH TEXT"


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


def translate_words(dict_words, token):
    for word in dict_words:
        if len(word) > 3:
            link = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=' + token + '&lang=en-ru&text=' + word
            response = requests.get(link, timeout=10)
            translate = json.loads(response.text)
            try:
                word_tr = translate['def'][0]['tr'][0]['text']
            except IndexError:
                word_tr = "none"
            dict_words[word][1] = word_tr
    return dict_words


def sort_words(dict_words):
    dict_words = sorted(dict_words.items(), key=lambda x: x[1], reverse=True)
    return dict_words

all_worlds = sort_words(translate_words(count_words(file), token))

for i in all_worlds:
    if len(i[0]) > 3:
        print(i[1][0], ": ", i[0], i[1][1])