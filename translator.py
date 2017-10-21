import re
import requests
import json


class Translator(object):

    def __init__(self, api_token, file_to_translate):
        self.api_token = api_token
        self.file_to_translate = file_to_translate

    def count_words(self):
        """
        The method "count_words" get file with text, count
        the words and put them to dictionary, where key is a
        word and value is a tuple: count and translate.
        """
        dict_words = {}
        with open(self.file_to_translate) as dict_of_words:
            text = re.sub('\W', ' ', dict_of_words.read())
            words = text.lower().split()
            for word in words:
                if len(word) > 3:
                    if word in dict_words:
                        dict_words[word][0] += 1
                    else:
                        # param is tuple [count, translate]
                        param = [1, ""]
                        dict_words[word] = param

        return dict_words

    def translate_words(self, dict_words):
        """
        The method "translate_words" get dictionary from method
        count_words and Yandex translate token(for more information
        about it https://tech.yandex.ru/dictionary/), and translate
        the words use Yandex dictionary API. Update translate in a
        tuple.
        """
        for word in dict_words:
            link = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=' + self.api_token + \
                   '&lang=en-ru&text=' + word + '&flags=4'
            response = requests.get(link, timeout=10)
            translate = json.loads(response.text)
            try:
                word_tr = translate['def'][0]['tr'][0]['text']
            except IndexError:
                word_tr = "none"
            dict_words[word][1] = word_tr

        return dict_words

    def sort_words(self, dict_words):
        """
        The function "sort_words" sort by number descending
        """
        dict_words = sorted(dict_words.items(), key=lambda x: x[1], reverse=True)

        return dict_words

token = "YOU YANDEX TRANSLATE TOKEN"
file = "FILE WITH ENGLISH TEXT"

translator = Translator(token, file)
dict_of_words = translator.count_words()
dict_of_translate_words = translator.translate_words(dict_of_words)
srt_dict_of_translate_words = translator.sort_words(dict_of_translate_words)

count = 0
for i in srt_dict_of_translate_words:
    print(i[1][0], ":", i[0], i[1][1])
    count += 1
print("\nCount: " + str(count))
