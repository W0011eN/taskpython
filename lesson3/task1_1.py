#Задание 1 
#Реализовать функцию, принимающую два числа (позиционные аргументы) и 
#выполняющую их деление. Числа запрашивать у пользователя, предусмотреть 
#обработку ситуации деления на ноль.

#Обработка исключения делинbя на ноль через конструкцию  try except

def fdiv (fdelim,fdelit):
    fres=fdelim/fdelit
    print("Результат деления: %0.2f" % fres)
try:
    fdiv(float(input('Введите делимое: ')),float(input('Введите делитель: ')))
except ZeroDivisionError:
    print("ERROR.\nДеление на ноль.")
