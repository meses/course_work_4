"""Для работы с классом вакансия"""
from API_Classes import HeadHunter
from utils import get_info_from_json, write_to_json

class Vacancy:
    """Работа с экземплярами класса Вакансия"""
    def __init__(self, vacancy_name:str, salary:dict, company_name:str, url:str):
        self.vacancy_name = vacancy_name
        self.__salary = salary
        self.company_name = company_name
        self.url = url

    def __str__(self):
        return f'{self.url}, {self.vacancy_name}, {self.salary}, {self.company_name}'

    @property
    def salary(self):
        if self.__salary is None:
            return {'from': 0, 'to': 0, 'currency': 'RUR', 'gross': False}
        else:
            return self.__salary




vacancy = HeadHunter().get_requests('Руководитель')
write_to_json(vacancy)
vacansy = get_info_from_json()['items']
#for i in vacansy:
# print(i['name'], i['salary'], i['employer']['name'], i['url'])
#object_counter = 0
#for i in vacansy:
#    str(object_counter) = Vacancy(vacansy['name'], vacansy['salary'], vacansy['employer']['name'], vacansy['url'])

vac_objs = [Vacancy(i['name'], i['salary'], i['company_name'], i['url']) for i in vacansy] # Создаёт экземпляры класса Vacancy из всего списка вакансий, полученных из файла
#vac_objs.sort(key=lambda x: x.salary['to'])
for i in range(len(vac_objs)):
    print(vac_objs[i])
print(len(vac_objs))

def sort_vacansy(vacansy_list):
    #vacansy_list[0].company_name = sort_attribute
    return vacansy_list.sort(key=lambda x: x.company_name)

#company_name = vac_objs[0].company_name
#print(sort_vacansy(vac_objs))


