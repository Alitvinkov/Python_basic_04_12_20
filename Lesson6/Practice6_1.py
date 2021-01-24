# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность
# первого состояния (красный)составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

import time
from itertools import cycle


class TrafficLight:
    __colors = ('Red', 'Yelow', 'Green')

    def __init__(self):
        self.__color = self.__colors[0]

    def init(self):
        pass

    def runing(self):
        light_time = (7, 2, 10)
        for trafic_light in cycle(zip(self.__colors, light_time)):
            self.__color = trafic_light[0]
            secund = trafic_light[1]
            while secund:
                print(f'{self.__color} - {secund}')
                secund -= 1
                time.sleep(1)


light = TrafficLight()
light.runing()
