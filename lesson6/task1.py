#Задание 1
#Создать класс TrafficLight (светофор).
#    определить у него один атрибут color (цвет) и метод running (запуск);
#    атрибут реализовать как приватный;
#    в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#    продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#    переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#    проверить работу примера, создав экземпляр и вызвав описанный метод.

from itertools import cycle
from time import sleep

class TrafficLight:

    __color__wait=cycle([{'color':'Красный','wait':7},
                  {'color':'Желтый','wait':2},
                  {'color':'Зеленый','wait':5}])
    def run_light(self):
        light = next(self.__color__wait)
        print(f"Цвет {light['color']}, ожидание {light['wait']} сек.")
        sleep(light['wait'])

_TrafficLight=TrafficLight()

_TrafficLight.run_light()
_TrafficLight.run_light()
_TrafficLight.run_light()
_TrafficLight.run_light()
