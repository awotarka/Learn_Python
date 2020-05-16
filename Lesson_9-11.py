import random
import json
 # код отвечает на вопросы да-нет,запоминает уже заданные вопросы и распознает неточные вопросы с точностью 0.5
 # задание 11 урока: апдейт для 9 урока, добавлен файл json '9.json', в который записываются заданные вопросы
 # файл '9.json' не должен быть пустым, изначально должен содержать '{}'



def compare(s1, s2):
    s1, s2 = [s.lower() for s in [s1, s2]]
    ngrams = [s1[i:i+3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count / max(len(s1), len(s2))


# эта функция берет словарь уже заданных вопросов и новый заданный вопрос, для уже заданого вопроса делает следующее:
#берет уже заданный вопрос и разбивает на слова, берет новый вопрос и разбивает на слова, для каждого слова из двух
# вопросов по порядку вычисляет коэффициент похожести, находит среднее арифметическое коэффициентов похожести,
# так для каждого из уже заданных вопросов, выбирает из словаря вопросов тот,у которого больший коэффициент похожести,
# проверяет, больше ли он 0.5, если больше то выдает уже заданный вопрос, если меньше, то не выдает ничего


def find_sim_quest(k, questions):
    similarities = {}
    for q in questions:
        sum_similarity = 0
        q_words = q.split()
        question_words = k.split()
        for i in range(min(len(q_words), len(question_words))):
            sum_similarity += compare(q_words[i], question_words[i])
        similarities[sum_similarity / min(len(q_words), len(question_words))] = q
    if max(similarities.keys()) >= 0.5:
        return similarities[max(similarities.keys())]
    else:
        return None


k = input('')
questions = data = json.load(open('9.json')) or {} #читает словарь вопросов из файла json

# принимает вопросы пока не передастся пустая строка
# рандомно отвечает да нет на новый вопрос, на уже заданный отвечает сохраненным ответом


while k:
    if not questions or not find_sim_quest(k, questions):
        answer = 'yes' if random.randint(0, 10) <= 5 else 'no'
        questions[k] = answer
        print(answer)
    else:
        print('this question has been already asked' + ', answer: ' + questions[find_sim_quest(k, questions)])
    k = input('')

#сохраняет новые вопросы в json

with open('9.json', 'w') as outfile:
    outfile.write(json.dumps(questions, indent=2))

data = json.load(open('9.json'))
print(questions)
