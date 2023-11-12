'''Конвертирование из CSV в JSON формат'''
import csv

import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
RESULT = {}

def task() -> None:
    with open(INPUT_FILENAME, 'r') as f:
        reader = csv.DictReader(f, delimiter=",")
        RESULT = {}
        for row in reader:
            for column, value in row.items():
                RESULT.setdefault(column, []).append(value)

    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
        json.dumps(RESULT, indent=4)
    return print(json.dumps(RESULT, indent=4))


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
