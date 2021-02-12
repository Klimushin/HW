# Вспоминаем работу с файлом. Есть файл, 
# в котором много англоязычных текстовых строк. 
# Считаем частоту встретившихся слов в файле, 
# но через функции и map, без единого цикла!

with open('1.txt', 'r') as file:
# читаем файл, убираем знаки пунктуации,
# приводим к нижнему регистру и сплитим текст 
    data = file.read() \
        .replace('\n', '') \
        .replace('.', '') \
        .replace(',', '') \
        .replace('(', '') \
        .replace(')', '') \
        .replace("'", '') \
        .lower()
    list_all_words = data.split(' ')


def some_func(item):
    return list_all_words.count(item)
# функция считает количество повторений слова
# в списке


unique_words = list(set(list_all_words))
# находим уникальные слова в списке, 
# преобразовав его во множество.
count_of_words = map(some_func, unique_words)

result_zip = zip(unique_words, count_of_words)
print(dict(result_zip))
