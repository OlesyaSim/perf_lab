import json
import sys


def update_values(tests, values):
    if isinstance(tests, list):
        for item in tests:
            update_values(item, values)
    elif isinstance(tests, dict):
        if 'id' in tests and 'value' in tests:
            test_id = tests['id']
            for value_item in values['values']:
                if value_item['id'] == test_id:
                    tests['value'] = value_item['value']
        for key, value in tests.items():
            if isinstance(value, (dict, list)):
                update_values(value, values)


if len(sys.argv) != 3:
    print("Введите команду: python task3.py <файл_тестов> <файл_значений>")
else:
    tests_file = sys.argv[1]
    values_file = sys.argv[2]

    try:
        with open(tests_file, 'r') as tests_file:
            tests_data = json.load(tests_file)
        with open(values_file, 'r') as values_file:
            values_data = json.load(values_file)
        update_values(tests_data, values_data)
        with open('report.json', 'w') as report_file:
            json.dump(tests_data, report_file)
        print("Обновленная структура сохранена в report.json")
    except FileNotFoundError:
        print("Один или несколько файлов не найдены")
    except json.JSONDecodeError:
        print("Возникла ошибка при считывании json данных из файлов")
