#Задание 4
#Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
#При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

f1 =open('task4_1.txt','r')
f2 =open('task4_2.txt','w+')
chisl_list=["Один","Два","Три","Четыре"]
try:
        lst=[]
        for line in f1.readlines():
                lst.extend(line.rstrip().split(' '))
        print(lst)
        n=0
        for i in range(0, len(lst), 3):
                lst[i]=chisl_list[n]
                n+=1
        print(lst)
        for j in range(2,len(lst),3):
                f2.writelines(lst[j-2]+lst[j-1]+lst[j]+'\n')
except IOError:
        print("Error file I/O ")

finally:
        f1.close()
        f2.close()
