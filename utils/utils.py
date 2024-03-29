import os.path

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


def is_get_top():
    """Валидация введённого значения для вывода топа вакансий"""
    is_top = ''
    while is_top not in ['1', '2']:
        is_top = input('Вывести топ вакансий по зарплате?\n1 - Да\n2 - Нет\n')
    return is_top

def how_mutch_vacansies_show():
    """Валидация введённого значения для количества вакансий"""
    count_vacancies = ''
    while count_vacancies.isdigit() == False:
        count_vacancies = input('Сколько вакансий показать? ')
    return int(count_vacancies)

