"""Работа с API"""
from abc import ABC, abstractmethod
import requests
import os

key = os.getenv("SUPERJOB_KEY")

class ABCEngine(ABC):

    @abstractmethod
    def __init__(self, url=''):
        pass

    @abstractmethod
    def get_requests(self, vacancy_name: str = ''):
        pass

    @staticmethod
    @abstractmethod
    def data_formatting(item):
        pass


class HeadHunter(ABCEngine):

    def __init__(self, url=f'https://api.hh.ru/vacancies'):
        self.__url = url

    @property
    def url(self):
        return self.__url


    @staticmethod
    def data_formatting(item):
        """Форматирование данных, полученных по запросу к HeadHunter"""
        item_dict = {}
        item_dict['name'] = item['name']
        item_dict['salary'] = set_correct_salary_hh(item['salary'])
        item_dict['company_name'] = item['employer']['name']
        item_dict['url'] = item['alternate_url']
        return item_dict

    def get_requests(self, vacancy_name:str = 'Разработчик'):
        """Функция для получения вакансий с HH с заданным поисковым запосом"""
        self.vacancy_name = vacancy_name
        data = {'items':[]}
        for i in range(1, 11):
            response = requests.get(self.url, params = {'User-Agent': 'Mozilla/5.0', # Должен быть агент
                                                        'text': f'{self.vacancy_name}', # Текст фильтра по вакансии
                                                        'area': '113', # Указание области (113 - Россия)
                                                        'per_page': 50, # Кол-во вакансий на одной странице
                                                        'page': str(i) # Индекс страницы
                                                        })
            if response.status_code == 200:
                for item in response.json()['items']:
                    data['items'].append(self.data_formatting(item))
        return data



class SuperJob(ABCEngine):

    def __init__(self, url=f'https://api.superjob.ru/2.0/vacancies/'):
        self.__url = url

    @property
    def url(self):
        return self.__url

    @staticmethod
    def data_formatting(item):
        """Форматирование данных, полученных по запросу к SuperJob"""
        item_dict = {}
        item_dict['name'] = item['profession']
        item_dict['salary'] = set_correct_salary_sj([item['payment_from'], item['payment_to'], item['currency']])
        item_dict['company_name'] = item['firm_name']
        item_dict['url'] = item['link']
        return item_dict

    def get_requests(self, vacancy_name:str = 'Разработчик'):
        """Функция для получения вакансий с HH с заданным поисковым запосом"""
        self.vacancy_name = vacancy_name
        headers = {
           'X-Api-App-Id': key,
        }
        data = {'items': []}
        for i in range(1, 11):
            response = requests.get(f'{self.url}?keyword={self.vacancy_name}&count=50&page={i}', headers=headers)
            if response.status_code == 200:
                for item in response.json()['objects']:
                    data['items'].append(self.data_formatting(item))
        return data

def set_correct_salary_sj(salary_original) -> dict:
    """Приводит к единому виду зарплату с SuperJob"""
    correct_salary = {}
    correct_salary['from'] = salary_original[0]
    correct_salary['to'] = salary_original[1]
    if salary_original[2] == 'rub':
        correct_salary['currency'] = "RUR"
    else:
        correct_salary['currency'] = salary_original[2]
    correct_salary['gross'] = False
    return correct_salary


def set_correct_salary_hh(salary_original) -> dict:
    """Приводит к единому виду зарплату с hh"""
    if salary_original is None:
        correct_salary = {"from": 0,
                          "to": 0,
                          "currency": "RUR",
                          "gross": False}
    elif salary_original['from'] is None:
        salary_original['from'] = 0
        correct_salary = salary_original
    elif salary_original['to'] is None:
        salary_original['to'] = 0
        correct_salary = salary_original
    else:
        correct_salary = salary_original
    return correct_salary

