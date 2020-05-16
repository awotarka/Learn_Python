#реализовано сложение 2+2 = 5, остальные целые числа складываются как обычно


class VolshebniyInt(int):
    def __add__(self, x):
        if self == 2:
            return super().__add__(x+1)
        else:
            return super().__add__(x)


#y = VolshebniyInt(2)
#print(y+2)

#реализован список который не принимает в себя больше 10 элементов

class ShortList(list):

    def __init__(self, x):
        if len(x) > 10:
            raise ValueError('>10')
        else:
            super().__init__(x)

    def append(self, x):
        if len(self) == 10: raise ValueError('>10')
        else: super().append(x)


y = ShortList([1, 2, 3, 4, 5, 6, 7])
y.append(11)

#реализован класс который превращает лист в уникальный лист(можно было сделать просто через функцию, но попросили класс)

class UniqueList(list):

    def unique(self):
        return list(set(self))


s = UniqueList([1, 1, 1, 2, 3, 4, 5, 5, 5])

print(s.unique())