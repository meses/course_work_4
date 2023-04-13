
import json
import os.path
from Utils.API_Classes import HeadHunter, SuperJob


#filename = 'data.json'

def write_to_json(data: dict, filename: str):
    """Метод записи данных в json"""
    #with open(filemname, 'a', encoding='UTF-8') as file:
    #    json.dump(data, file, indent=4, ensure_ascii=False)
    with open(filename, 'r', encoding='UTF-8') as file:
        old_data = json.load(file)
    for i in data['items']:
        old_data['items'].append(i)
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump(old_data, file, indent=4, ensure_ascii=False)

def get_info_from_json(filename: str) -> dict:
    """Выводит информацию о вакансиях из файла"""
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data

def clear_json(filename: str):
    with open(filename, 'w') as file:
        basic_data = {}
        basic_data = {'items': []}
        json.dump(basic_data, file, indent=4, ensure_ascii=False)
        #file.write('')

#clear_json('../Utils/data.json')

def is_empty_file(filename: str) -> bool:
    """Проверяет существует ли файл с данными о вакансиях и пустой ли он"""
    if not os.path.isfile(filename):
        return True
    elif os.path.isfile(filename) and os.path.getsize(filename) <= 21:
        return True
    elif os.path.getsize(filename) > 21:
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

def get_filtered_vacancies(user_platform, filter_word, filename) -> list:
    """Исходя из выбранной платформы, формируется список вакакнсий найденных по запросу пользователя"""
    filtered_vacancies = []
    if user_platform == '1':
        vacancy = HeadHunter().get_requests(filter_word)
        write_to_json(vacancy, filename)
        vacansy = get_info_from_json(filename)['items']
        for i in vacansy:
            filtered_vacancies.append(i)
    elif user_platform == '2':
        vacancy = SuperJob().get_requests(filter_word)
        write_to_json(vacancy, filename)
        vacansy = get_info_from_json(filename)['items']
        for i in vacansy:
            filtered_vacancies.append(i)
    elif user_platform == '3':
        vacancy = HeadHunter().get_requests(filter_word)
        write_to_json(vacancy, filename)
        vacancy = SuperJob().get_requests(filter_word)
        write_to_json(vacancy, filename)
        vacansy = get_info_from_json(filename)['items']
        for i in vacansy:
            filtered_vacancies.append(i)
    elif user_platform == '0':
        vacansy = get_info_from_json(filename)['items']
        for i in vacansy:
            if filter_word.lower() in str(i['name']).lower():
                filtered_vacancies.append(i)
    else:
        print('Что-то пошло не так')
    return filtered_vacancies
