#Задание 3
#Реализовать базовый класс Worker (работник).
#    определить атрибуты: name, surname, position (должность), income (доход);
#    последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
#    создать класс Position (должность) на базе класса Worker;
#    в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
#    проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name= name
        self.surname= surname
        self.position=position
        self._income={'wage':wage,'bonus':bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())
fname=input('Введите имя:')
lname=input('Введите фамилию:')
pos = input('Введите должность:')
wg= int(input('Введите оклад:'))
bon= int(input('Введите премию:'))
worker = Position(fname, lname, pos, wg, bon)
print(worker.get_full_name())
print(worker.position)
print(worker.get_total_income())

class Road:
    def __init__ (self, lenght, wight):
        self._lenght=lenght
        self._wight=wight
    def mass_asf(self,mass_asf_1m2,thickness):
        return self._lenght*self._wight*mass_asf_1m2*(thickness/100.0)
    
road = Road(int(input('Введите длину дороги в метрах: ')), int(input('Введите ширину дороги в метрах: ')))
mass_road=road.mass_asf(int(input('Введите массу асфальта на 1 метр кв. в килограммах: ')), int(input('Введите толщину покрытия в сантиметрах: ')))
print(f'Суммарный вес асфальта для дороги = {mass_road/1000} тонн') 