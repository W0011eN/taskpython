#Задание 2
#Пользователь вводит время в секундах. 
#Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк.

print ("Введите время в секундах:")
times = int( input() )
second = times % 60
times = times / 60
minute = times % 60
times = times / 60
hour = times
print ("%02d:%02d:%02d" % (hour,minute,second))
