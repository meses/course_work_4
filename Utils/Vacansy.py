"""Для работы с классом вакансия"""
class Vacancy:
    """Работа с экземплярами класса Вакансия"""
    def __init__(self, vacancy_name:str, salary:dict, company_name:str, url:str):
        self.__vacancy_name = vacancy_name
        self.__salary = salary
        self.__company_name = company_name
        self.__url = url

    def __str__(self):
        return f'{self.__url}, {self.__vacancy_name}, {self.__salary}, {self.__company_name}'

    def __lt__(self, other):
        if type(other) not in (Vacancy):
            raise TypeError('Аргумент должен быть типом Vacancy')
        else:
            return self.__salary['from'] < other.salary['from']

    def __gt__(self, other):
        if type(other) not in (Vacancy):
            raise TypeError('Аргумент должен быть типом Vacancy')
        else:
            return self.__salary['from'] < other.salary['from']

    @property
    def salary_for_print(self):
        if self.__salary['from'] == 0:
            self.__salary['from'] = 'Не указана'
        elif self.__salary['to'] == 0:
            self.__salary['to'] = 'Не указана'
        return self.__salary

    @property
    def salary(self):
        return self.__salary

    @property
    def url(self):
        return self.__url

    @property
    def vacancy_name(self):
        return self.__vacancy_name

    @property
    def company_name(self):
        return self.__company_name

def top_vacancies(vacancies:list, top_n:int) -> list:
    """Возвращает список топ N вакансий по зарплате"""
    vacancies.sort(key=lambda x: x.salary['from'], reverse=True)
    return vacancies[:top_n]

def show_vacancies(vacancies:list):
    """Выводит на экран список вакансий"""
    for i in range(len(vacancies)):
        print(f"url: {vacancies[i].url}, "
              f"Название: {vacancies[i].vacancy_name}, "
              f"Зарплата от: {vacancies[i].salary_for_print['from']}, "
              f"Зарплата до: {vacancies[i].salary_for_print['to']}, "
              f"Компания: {vacancies[i].company_name}")

