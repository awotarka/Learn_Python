class Person:
    def __init__(self, name, age, height, weigh, adress):
        self.name = name
        self.age = age
        self.height = height
        self.weigh = weigh
        self.adress = adress
    def _show_(self):
        print('\n', 'Имя: ',self.name,'\n','Возраст: ', self.age, '\n', 'Рост: ', self.height, '\n', 'Вес: ',self.weigh,'\n', 'Адрес: ', self.adress)
Viacheslav = Person('Вячеслав', 31, 175, 78, 'г. Пермь')
Viacheslav._show_()
Natasha = Person('Наташа', 22, 150, 80, 'г. Саратов')
#рост
A=120
for obj in len(Natasha):
    if obj == A:
        print(obj)
    elif obj == 'Наташа':
        print(obj)


def search():
    smth1 = input()
    if smth1>=118 and smth1<=121:
        print("is")
    elif smth1=='Наташа' or 'наташа' or 'нташа':
        print("is")
    else:
        print("is not")
