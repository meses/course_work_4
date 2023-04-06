
import json
import os.path

filename = 'data.json'
def set_correct_salary_hh(salary) -> dict:
    """Приводит к единому виду зарплату с hh"""
    if salary is None:
        correct_salary = {"from": None,
                "to": None,
                "currency": "RUR",
                "gross": None}
    else:
        correct_salary = salary
    return correct_salary

def write_to_json(data: dict, filemname: str = filename):
    """Метод записи данных в json"""
    with open(filemname, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def get_info_from_json(filename: str = filename) -> dict:
    """Выводит информацию о вакансиях из файла"""
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data

def is_empty_file(filename: str = filename) -> bool:
    """Проверяет существует ли файл с данными о вакансиях и пустой ли он"""
    if not os.path.isfile(f'../Utils/{filename}'):
        return True
    elif os.path.isfile(f'../Utils/{filename}') and os.path.getsize(f'../Utils/{filename}') == 0:
        return True
    elif os.path.getsize(f'../Utils/{filename}') != 0:
        return False

