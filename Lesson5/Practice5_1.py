# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

new_file = open('practice5_1.txt', 'w')

while True:
    text = input('Vvedite slovo ili predlogenie. Okon4anie vvoda nagmite ENTER\n>>>>>')
    new_file.write(str(text) + '\n')
    if not text:
        break
new_file.close()
