import json


def update_values(tests, values):
    if isinstance(tests, list):
        for item in tests:
            update_values(item, values)
    elif isinstance(tests, dict):
        if 'id' in tests and 'value' in tests:
            test_id = tests['id']
            if test_id in values:
                tests['value'] = values[test_id]
        for key, value in tests.items():
            if isinstance(value, (dict, list)):
                update_values(value, values)


try:
    with open('tests.json', 'r') as tests_file:
        tests_data = json.load(tests_file)

    with open('values.json', 'r') as values_file:
        values_data = json.load(values_file)

    update_values(tests_data, values_data)

    with open('report.json', 'w') as report_file:
        json.dump(tests_data, report_file)

    print("Обновленная структура сохранена в report.json")

except FileNotFoundError:
    print("Один или несколько файлов не найдены")
except json.JSONDecodeError:
    print("Возникла ошибка при считывании json данных из файлов")
