import json
from abc import abstractmethod
from classes.engine_classes import HeadHunter, SuperJob


class ABCSaver:
    """Отвечает за сохранение, получение, удаление и поиск где угодно – файлы, апи, бд, json"""

    @abstractmethod
    def write_to_json(self, data, path):
        pass

    @abstractmethod
    def get_info_from_json(self, path):
        pass

    @abstractmethod
    def clear_json(self, path):
        pass

    @abstractmethod
    def get_filtered_vacancies(self, user_platform, filter_word, path):
        pass


class JSONSaver(ABCSaver):
    """Отвечает за сохранение, получение, удаление и поиск в файле json"""
    def write_to_json(self, data: dict, filename: str):
        """Метод записи данных в json"""
        with open(filename, 'r', encoding='UTF-8') as file:
            old_data = json.load(file)
        for i in data['items']:
            old_data['items'].append(i)
        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(old_data, file, indent=4, ensure_ascii=False)

    def get_info_from_json(self, filename: str) -> dict:
        """Выводит информацию о вакансиях из файла"""
        with open(filename, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        return data

    def clear_json(self, filename: str):
        """Очистка файла для новой записи"""
        with open(filename, 'w') as file:
            basic_data = {}
            basic_data = {'items': []}
            json.dump(basic_data, file, indent=4, ensure_ascii=False)

    def get_filtered_vacancies(self, user_platform, filter_word, filename) -> list:
        """Исходя из выбранной платформы, формируется список вакакнсий найденных по запросу пользователя"""
        filtered_vacancies = []
        if user_platform == '1':
            vacancy = HeadHunter().get_requests(filter_word)
            self.write_to_json(vacancy, filename)
            vacansy = self.get_info_from_json(filename)['items']
            for i in vacansy:
                filtered_vacancies.append(i)
        elif user_platform == '2':
            vacancy = SuperJob().get_requests(filter_word)
            self.write_to_json(vacancy, filename)
            vacansy = self.get_info_from_json(filename)['items']
            for i in vacansy:
                filtered_vacancies.append(i)
        elif user_platform == '3':
            vacancy = HeadHunter().get_requests(filter_word)
            self.write_to_json(vacancy, filename)
            vacancy = SuperJob().get_requests(filter_word)
            self.write_to_json(vacancy, filename)
            vacansy = self.get_info_from_json(filename)['items']
            for i in vacansy:
                filtered_vacancies.append(i)
        elif user_platform == '0':
            vacansy = self.get_info_from_json(filename)['items']
            for i in vacansy:
                if filter_word.lower() in str(i['name']).lower():
                    filtered_vacancies.append(i)
        else:
            print('Что-то пошло не так')
        return filtered_vacancies

