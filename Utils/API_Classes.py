"""Работа с API"""
import requests
import json
#from Utils.utils import set_correct_salary_hh, set_correct_salary_sj

SUPERJOB_KEY = 'v3.r.137479068.1515f066f0bc16a3615c4a0f679c0d342111cfa3.f4d6e1bdbd401e9c88651e580f6517bef79b15f3'

class Main_API:
    pass


class HeadHunter(Main_API):
    def __init__(self):
        self.url = f'https://api.hh.ru/vacancies'


    def get_requests(self, vacancy_name:str = 'Разработчик'):
        """Функция для получения вакансий с HH с заданным поисковым запосом"""
        data = {'items':[]}
        for i in range(1, 11):
            response = requests.get(self.url, params = {'User-Agent': 'Mozilla/5.0', # Должен быть агент
                                                        'text': f'{vacancy_name}', # Текст фильтра по вакансии
                                                        'area': '113', # Указание области (113 - Россия)
                                                        'per_page': 50, # Кол-во вакансий на одной странице
                                                        'page': str(i) # Индекс страницы
                                                        })
            if response.status_code == 200:
                for j in response.json()['items']:
                    item_dict = {}
                    item_dict['name'] = j['name']
                    item_dict['salary'] = set_correct_salary_hh(j['salary'])
                    item_dict['company_name'] = j['employer']['name']
                    item_dict['url'] = j['alternate_url']
                    data['items'].append(item_dict)
        return data



class SuperJob(Main_API):
    def __init__(self):
        self.url = f'https://api.superjob.ru/2.0/vacancies/'

    def get_requests(self, vacancy_name:str = 'Разработчик'):
        """Функция для получения вакансий с HH с заданным поисковым запосом"""
        self.vacancy_name = vacancy_name
        headers = {
           'X-Api-App-Id': SUPERJOB_KEY,
        }
        data = {'items': []}
        for i in range(1, 11):
            response = requests.get(f'{self.url}?keyword={self.vacancy_name}&count=50&page={i}', headers=headers)
            if response.status_code == 200:
                for item in response.json()['objects']:
                    item_dict = {}
                    item_dict['name'] = item['profession']
                    item_dict['salary'] = set_correct_salary_sj([item['payment_from'], item['payment_to'], item['currency']]) #get_correct_sj_salary(str(item['payment_from']), str(item['payment_to']))
                    item_dict['company_name'] = item['firm_name']
                    item_dict['url'] = item['link']
                    data['items'].append(item_dict)

        return data

def set_correct_salary_sj(salary_original) -> dict:
    """Приводит к единому виду зарплату с SuperJob"""
    salary = {}
    salary['from'] = salary_original[0]
    salary['to'] = salary_original[1]
    if salary_original[2] == 'rub':
        salary['currency'] = "RUR"
    else:
        salary['currency'] = salary_original[2]
    salary['gross'] = False
    return salary


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
#test_hh = HeadHunter().get_requests()
#test_hh.get_requests()
#print(test_hh.get_info_from_json()['items'])
#vacansies = test_hh.get_info_from_json()['items']
#for i in vacansies:
#    print(i['name'])
#test_sj = SuperJob().get_requests()
#for i in test_sj['items']:
#    print(i)

