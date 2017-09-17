import functions

token = "YOU YANDEX TRANSLATE TOKEN"
file = "FILE WITH ENGLISH TEXT"


all_worlds = functions.sort_words(functions.translate_words(functions.count_words(file), token))

for i in all_worlds:
    if len(i[0]) > 3:
        print(i[1][0], ": ", i[0], i[1][1])