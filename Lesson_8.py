#код с урока 6 исправлен с соблюдением правил pep8

class Customer:
    def __init__(self, id, name, age, purchase_num, purchase_sum):
        self.name, self.age, self.purchase_num, self.purchase_sum
        = name, age, purchase_num, purchase_sum
        self.key = id  # primary_key

    def __repr__(self):
        return "{'name':'%s','age':%s,'num':%s,'sum':%s}"
        % (self.name, self.age, self.purchase_num, self.purchase_sum)

    def d(self):
        return {
            'name': self.name,
            'age': self.age,
            'num': self.purchase_num,
            'sum': self.purchase_sum}

lena = Customer(1, 'Лена', 20, 15, 22000)
artem = Customer(2, 'Артем', 30, 50, 7000)
lidia = Customer(3, 'Лидия', 24, 21, 3500)
fedor = Customer(4, 'Федор', 33, 5, 1000)
alexey = Customer(5, 'Алексей', 40, 114, 86000)
maria = Customer(6, 'Мария', 16, 70, 10000)
custs = {
    lena.key: lena.d(),
    artem.key: artem.d(),
    lidia.key: lidia.d(),
    fedor.key: fedor.d(),
    alexey.key: alexey.d(),
    maria.key: maria.d()
    }

# сделать поиск по параметрам

# 1) возраст < 30 лет


less_30 = []
for i in custs:
    if custs[i]['age'] < 30:
        less_30.append(custs[i])
print(less_30)

# 2)покупки от 1000 до 20000


purch_1000_to_20000 = []
for i in custs:
    if custs[i]['sum'] > 1000 and custs[i]['sum'] < 20000:
        purch_1000_to_20000.append((custs[i]['name'], custs[i]['sum']))

# сделать поиск нечетким

# сравнение имен


def compare(s1, s2):
    ngrams = [s1[i:i+3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count/max(len(s1), len(s2))
print(compare('Лодея', 'Лидия'))

# похожие имена


def near_search_names(s1):
    targets = []
    for i in custs:
        s2 = custs[i]['name']
        if compare(s1, s2) >= 0.3:
            targets.append((i, s2))
    return targets

# похожие суммы


def near_search_sum(n1):
    target_sum = []
    for i in custs:
        n2 = custs[i]['sum']
        if abs(n2-n1) <= 200:
            target_sum.append((i, custs[i]['name'], n2))
    return target_sum
print(near_search_names('Лидея'), near_search_sum(1100))
