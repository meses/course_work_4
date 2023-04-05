"""Для работы с классом вакансия"""
from API_Classes import HeadHunter

class Vacancy:
    """Работа с экземплярами класса Вакансия"""
    def __init__(self, vacancy_name:str, salary:dict, company_name:str, url:str):
        self.vacancy_name = vacancy_name
        self.salary = salary
        self.company_name = company_name
        self.url = url

    def __str__(self):
        return f'{self.url}, {self.vacancy_name}, {self.salary}, {self.company_name}'


vac_list = HeadHunter()
vacansy = vac_list.get_info_from_json()['items']
#for i in vacansy:
# print(i['name'], i['salary'], i['employer']['name'], i['url'])
#object_counter = 0
#for i in vacansy:
#    str(object_counter) = Vacancy(vacansy['name'], vacansy['salary'], vacansy['employer']['name'], vacansy['url'])

vac_objs = [Vacancy(i['name'], i['salary'], i['employer']['name'], i['url']) for i in vacansy] # Создаёт экземпляры класса Vacancy из всего списка вакансий, полученных из файла
for i in range(5):
    print(vac_objs[i].__str__())

