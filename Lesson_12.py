#созданы классы Male, Female, наследованные от Person, созданы методы для каждого из классов show_gender, marry, celebrate birthday
class Person:
    def __init__(self, name, surname, passport, age):
        self.name, self.surname, self.passport, self.age = name, surname, passport, age
        self.key = passport


class Female(Person):
    isMarried = False

    def show_gender(self):
        return 'female'

    def marry(self, new_surname):
        self.isMarried = True
        self.surname = new_surname
        print(self.isMarried, 'new_surname: ' + self.surname)

    def celebrate_birthday(self):
        self.age += 1


class Male(Person):
    isMarried = False

    def show_gender(self):
        return 'male'

    def marry(self):
        self.isMarried = True

    def celebrate_birthday(self):
        self.age += 1


anna = Female('anna', 'anna', 123, 12)
petr = Male('petr', 'ivanov', 233, 26)
print(anna.show_gender(), petr.show_gender(), anna.key)
anna.celebrate_birthday()
print(anna.isMarried, anna.age)
