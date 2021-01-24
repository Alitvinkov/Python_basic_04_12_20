# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, leng: float, widht: float):
         self._leng = leng
         self._widht = widht

    def mass_asphalt (self, square_sm_mass: float, thickness_sm: float):
        return self._leng * self._widht * square_sm_mass * thickness_sm / 1000

new_road = Road (20, 5000)
print(f'Trebuetsya asfalta {new_road.mass_asphalt(25,5):.1f} tonn')



