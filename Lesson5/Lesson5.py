# f = open('file.txt', 'w')  # 'r' po umolchaniyu regim zapisi 'w' nugno ukazivat EKSTRA
# data = ['stroka\n', 'stroka1\n', 'stroka2\n']
# f.writelines(data)
# content = f.readlines()
# content2 = f.readline()
# content3 = f.readline()
# for line in f:
# print(line)
# print(content)
# f.close()
# with open('file.txt') as f:
    # for line in f:
        # print(line)
# try:
# with open('file.txt') as f:
#     data = f.read()
# except (IOError, FileNotFoundError)
#     print('Proizowla owibka')
# print(data)

# with open('file2.txt', 'x') as f:
#     data = f.write('123')

# with open('file2.txt', 'a') as f:
#      data = f.write('\n new str')

# with open('file2.txt', 'r+') as f:
#     data = f.write('\n new str+')
#     print(f.name)
#     print(f.closed)
#     print(f.mode)

with open ('file.txt', 'r') as f:
    print(f.read(5))
#    print(f.read())
    print(f.tell())
    f.seek(0)
    print(f.read(6))
    print(f.tell())


