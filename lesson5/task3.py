#Задание 3
#Создать текстовый файл (не программно). Построчно записать фамилии сотрудников 
#и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет 
#оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт 
#средней величины дохода сотрудников.
#Пример файла:

#Иванов 23543.12
#Петров 13749.32

f =open('task3.txt','r')
try:
    lst = list()
    line_count = 0
    for line in f.readlines():
        lst.extend(line.rstrip().split(' '))
        line_count += 1
    print("Зарплата меньше 20тыс.:")
    sum=0
    for i in range(1,len(lst),2):
       z=float(lst[i])
       sum+=z
       if (z<20000):
           print(lst[i-1])
    print(f'Средняя зарблата сотрудников: {sum/line_count}')
except IOError:
        print("Error file I/O ")

finally:
        f.close()
