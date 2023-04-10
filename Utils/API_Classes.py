"""Работа с API"""
import requests
import json
from Utils.utils import set_correct_salary_hh, write_to_json


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
                                                        'per_page': 20, # Кол-во вакансий на одной странице
                                                        'page': str(i) # Индекс страницы
                                                        })
            for j in response.json()['items']:
                item_dict = {}
                item_dict['name'] = j['name']
                item_dict['salary'] = set_correct_salary_hh(j['salary'])
                item_dict['company_name'] = j['employer']['name']
                item_dict['url'] = j['url']
                data['items'].append(item_dict)
        return data
        #write_to_json('data.json', data)


class SuperJob(Main_API):
    pass

#test_hh = HeadHunter().get_requests()
#test_hh.get_requests()
#print(test_hh.get_info_from_json()['items'])
#vacansies = test_hh.get_info_from_json()['items']
#for i in vacansies:
#    print(i['name'])

