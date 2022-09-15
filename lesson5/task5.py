#Задание 5
#Создать (программно) текстовый файл, записать в него программно набор чисел,
#разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и 
#выводить её на экран.

f =open('task5.txt','w+')
try:
        while True:
                str=input()
                f.write(str+'\n')
                if str == "":
                        break
        f =open('task5.txt','r')
        lst = f.read().split()
        sum_total = 0
        for el in lst:
               sum_total += float(el)
        print("Сумма чисел: ", sum_total)
except IOError:
        print("Error file I/O ")

finally:
        f.close()
