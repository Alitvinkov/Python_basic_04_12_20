# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

line_count = 0
words_count = 0

with open('PRactice5_2.txt', 'r') as file:
    for line in file:
        line_count += 1
        line_words = len(line.split())
        words_count += line_words
        print(words_count)


