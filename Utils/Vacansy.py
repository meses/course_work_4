"""Для работы с классом вакансия"""
class Vacancy:
    """Работа с экземплярами класса Вакансия"""
    def __init__(self, vacancy_name:str, salary:dict, company_name:str, url:str):
        self.vacancy_name = vacancy_name
        self.salary = salary
        self.company_name = company_name
        self.url = url

    def __str__(self):
        return f'{self.url}, {self.vacancy_name}, {self.salary}, {self.company_name}'

    def __lt__(self, other):
        if type(other) not in (Vacancy):
            raise TypeError('Аргумент должен быть типом Vacancy')
        else:
            return self.salary['from'] < other.salary['from']

    def __gt__(self, other):
        if type(other) not in (Vacancy):
            raise TypeError('Аргумент должен быть типом Vacancy')
        else:
            return self.salary['from'] < other.salary['from']

    @property
    def salary_for_print(self):
        if self.salary['from'] == 0:
            self.salary['from'] = 'Не указана'
        elif self.salary['to'] == 0:
            self.salary['to'] = 'Не указана'
        return self.salary

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

