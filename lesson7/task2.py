from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_cloth_count(self):
        pass

class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def get_cloth_count(self):
        return self.v/6.5 + 0.5

class Suit(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def get_cloth_count(self):
        return self.h * 2 + 0.3


Coat1 = Coat(int(input ('Введите размер пальто: ')))
print(f'Расход ткани для пальто:{Coat1.get_cloth_count}')

Coat2 = Coat(int(input ('Введите размер пальто: ')))
print(f'Расход ткани для пальто:{Coat2.get_cloth_count}')

Suit1 = Suit(int(input ('Введите рост костюма: ')))
print(f'Расход ткани для костюма:{Suit1.get_cloth_count}')

Suit2 = Suit(int(input ('Введите рост костюма: ')))
print(f'Расход ткани для костюма:{Suit2.get_cloth_count}')