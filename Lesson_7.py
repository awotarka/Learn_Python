from pprint import pprint
from itertools import product
class Person:
    def __init__(self, name, surname,father_name, age, address):
        self.name,self.surname, self.father_name, self.age, self.address = name, surname, father_name, age, address
        self.key = (name, address)

    def __repr__(self):
        return "Person('%s', '%s', '%s', %s, '%s')" % (self.name,self.surname,self.father_name, self.age, self.address)

    def __eq__(self, obj):
        if type(obj) == Person:
            return (self.name, self.surname, self.father_name, self.age, self.address) == (obj.name, obj.surname,
                                                                                           obj.father_name, obj.age,
                                                                                           obj.address)
        elif type(obj) == str:
            return self.fuzzy_compare(obj)
        else:
            return self.__repr__() == obj.__repr__()

    ## реализация нечеткого запроса
    ADDRESS_WORDS = {'дом', 'улица', 'живет'}
    NAME_WORDS = {'имя', 'зовут'}
    AGE_WORDS = {'возраст', 'старше', 'младше'}
    SURNAME_WORDS ={'фамилия'}
    FATHERNAME_WORDS = {'отчество', 'по-батюшке'}

    def compare(self, s1, s2):
        s1, s2 = [s.lower() for s in [s1,s2]]
        ngrams = [s1[i:i+3] for i in range(len(s1))]
        count = 0
        for ngram in ngrams:
            count += s2.count(ngram)
        return count / max(len(s1),len(s2))

    def int_val(self,s):
        try:
            return int(s)
        except ValueError:
            return 0

    def fuzzy_compare(self, query):
        def by_address(Q):
            Q = Q - self.ADDRESS_WORDS
            W = set(self.address.split())
            rez = []
            for a, b in product(Q, W):
                rez += [(self.compare(a, b), a, b)]
            return max(rez)[0]

        def by_age(Q):
            q_age = max([self.int_val(q) for q in Q])
            if 'старше' in Q:
                return q_age < self.age
            if 'младше' in Q:
                return q_age > self.age
            return q_age + 5 >= self.age >= q_age - 5

        def by_name(Q):
            Q = Q - self.NAME_WORDS
            W = set(self.name.split())
            rez = []
            for a, b in product(Q, W):
                rez += [(self.compare(a, b), a, b)]
            return max(rez)[0]
        def by_surname(Q):
            Q = Q - self.SURNAME_WORDS
            W = set(self.surname.split())
            rez = []
            for a, b in product(Q, W):
                rez += [(self.compare(a, b), a, b)]
            return max(rez)[0]

        def by_fathername(Q):
            Q = Q - self.FATHERNAME_WORDS
            W = set(self.father_name.split())
            rez = []
            for a, b in product(Q, W):
                rez += [(self.compare(a, b), a, b)]
            return max(rez)[0]


        q_words = set(query.split())
        score = 0
        for m_words, method in zip([self.ADDRESS_WORDS, self.NAME_WORDS, self.AGE_WORDS, self.SURNAME_WORDS,
                                    self.FATHERNAME_WORDS],
                        [by_address, by_name, by_age, by_surname, by_fathername]):
            if m_words & q_words:
                score += method(q_words)
        return score > 0.49


lena = Person("Лена","Ленина", "Александровна", 19, "Пушкина, 14, 115")
oleg = Person("Олег", "Ленский", "Михайлович", 34, "Ленского, 10, 11")
olga = Person("Ольга","Хоритонова", "Константиновна",  28, "Онегина,  11,  12")
nata = Person("Наташа","Шемякина", "Александровна", 17, "Ростова,  16,  15")

people = {
    lena.key: lena,
    oleg.key: oleg,
    olga.key: olga,
    nata.key: nata,
}

##pprint(people)

queries = [
    'имя Ольга', 'возраст 30', 'старше 20', 'младше 20', 'живет на Пушкина', 'дом 10', 'фамилия ростова', 'зовут нташа',
    'женского пола', 'фамилия Ленна', 'по-батюшке Александровна',
]

for query, person in product(queries, people.values()):
    if person == query:
       pprint((query,person))


##Добавлены фамилия и отчество, разбитые в другие поля
##Ошибка в видео - self для функций не был указан
