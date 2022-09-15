#Задание 2
#Создать текстовый файл (не программно), сохранить в нём несколько строк,
#выполнить подсчёт строк и слов в каждой строке.

f =open('task2.txt','r')
i=0
try:
  for line in f:
    i=i+1
    print (f'Количество слов {len(line.split())} в строке {i}')
    print (line)
except IOError:
        print("Error file I/O ")

finally:
        print(f'Количество строк: {i}')
        f.close()
