"""Работа с API"""
import requests
import json


class Main_API:
    pass


class HeadHunter(Main_API):
    def __init__(self):
        self.url = f'https://api.hh.ru/vacancies'


    def get_requests(self):
        params = {
            'User-Agent': 'Mozilla/5.0', # Должен быть агент
            'text': 'Водитель', # Текст фильтра по вакансии
            'area': '113', # Указание области (113 - Россия)
            'per_page': 5, # Кол-во вакансий на одной странице
            'page': 0 # Индекс страницы
        }
        response = requests.get(self.url, params)
        res = response.json()
        self.write_to_json('data.json', res)
        '''
        for i in range(1, 11):
            response = requests.get(self.url, params) #params={'User-Agent': 'Mozilla/5.0', 'area': '113', 'per_page': '100', 'page': str(i)})
            if i == 1:
                res = response.json()
            else:
                res['items'].append(response.json()['items'][0])
        self.write_to_json('data.json', res)
        '''

    @staticmethod
    def write_to_json(filemname: str, data: dict):
        """Метод записи данных в json"""
        with open(filemname, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def get_info_from_json(self):
        """Выводит информацию о вакансиях из файла"""
        filename = 'data.json'
        with open(filename, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        return data


class SuperJob(Main_API):
    pass

test_hh = HeadHunter()
#test_hh.get_requests()
#print(test_hh.get_info_from_json()['items'])
#vacansies = test_hh.get_info_from_json()['items']
#for i in vacansies:
#    print(i['name'])

