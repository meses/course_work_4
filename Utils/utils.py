
import json
import os.path

#filename = 'data.json'
def set_correct_salary_hh(salary) -> dict:
    """Приводит к единому виду зарплату с hh"""
    if salary is None:
        correct_salary = {"from": 0,
                "to": 0,
                "currency": "RUR",
                "gross": False}
    elif salary['from'] is None:
        salary['from'] = 0
        correct_salary = salary
    elif salary['to'] is None:
        salary['to'] = 0
        correct_salary = salary
    else:
        correct_salary = salary
    return correct_salary

def write_to_json(data: dict, filemname: str):
    """Метод записи данных в json"""
    with open(filemname, 'a', encoding='UTF-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def get_info_from_json(filename: str) -> dict:
    """Выводит информацию о вакансиях из файла"""
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data

def clear_json(filename: str):
    with open(filename, 'w') as file:
        file.write('')

def is_empty_file(filename: str) -> bool:
    """Проверяет существует ли файл с данными о вакансиях и пустой ли он"""
    if not os.path.isfile(filename):
        return True
    elif os.path.isfile(filename) and os.path.getsize(filename) == 0:
        return True
    elif os.path.getsize(filename) != 0:
        return False

def select_services():
    """Функция выбора платформы для загрузки данных"""
    available_services = {'1':'HeadHunter', '2':'SuperJob', '3':'Со всех сразу'}
    user_choise_platform = None
    while user_choise_platform not in available_services.keys():
        print(f'Выберите с какой платформы хотите загрузить вакансии:')
        for key, value in available_services.items():
            print(key, "-", value)
        user_choise_platform = input()
        if user_choise_platform in available_services.keys():
            return user_choise_platform

def file_or_new_request(filename):
    """Функция для выбора работы с файлом или загрузки новых данных с платформ"""
    if is_empty_file(filename) == False:
        user_input = input('Уже есть загруженные данные. Использовать их?\n1 - Да\n2 - Нет, хочу загрузить новые\n')
        if user_input == '1':
            choise_platform = '0'
        else:
            choise_platform = select_services()
    else:
        choise_platform = select_services()
    return choise_platform

def vacancy_filter(dataset, filter_word):
    pass

