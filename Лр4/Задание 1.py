'''Поиск суммы произведений из списка словарей при помощи модуля json'''
import json

FILENAME = "input.json"
LIST1 =[]
LIST_SCORE = []
LIST_WEIGHT = []

def task() -> float:
    with open(FILENAME) as f:
        data = json.load(f)
        #print(data)
        LIST_SCORE = [item['score'] for item in data]
        LIST_WEIGHT = [item['weight'] for item in data]
        #print(LIST_SCORE)
        #print(LIST_WEIGHT)
        A = sum(LIST_SCORE)
        #print(A)

    return round(A, 3)

print(task())
