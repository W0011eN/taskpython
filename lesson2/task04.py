#Задание 4 
#Пользователь вводит строку из нескольких слов, разделённых пробелами.
#Вывести каждое слово с новой строки. Строки нужно пронумеровать. 
#Если слово длинное, выводить только первые 10 букв в слове.

my_list = input("Введите элементы списка: ").split()
for i in range(0,len(my_list)):
    if len(my_list[i])<10:
        print(my_list[i])
