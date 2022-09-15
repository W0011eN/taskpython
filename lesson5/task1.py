#Задание 1
#Создать программный файл в текстовом формате, записать в него построчно данные,
#вводимые пользователем. Об окончании ввода данных будет свидетельствовать
#пустая строка.

f =open('task1.txt','w+')
try:
  while True:
    str=input()
    f.write(str+'\n')
    if str == "":
      break
except IOError:
        print("Error file I/O ")

finally:
        f.close()
