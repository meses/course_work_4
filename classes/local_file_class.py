import json
from abc import abstractmethod
from classes.engine_classes import HeadHunter, SuperJob


class ABCSaver:
    """Отвечает за сохранение, получение, удаление и поиск где угодно – файлы, апи, бд, json"""

    @abstractmethod
    def write(self, data, path):
        pass

    @abstractmethod
    def read(self, path):
        pass

    @abstractmethod
    def clear(self, path):
        pass

    @abstractmethod
    def get_filtered_vacancies(self, user_platform, filter_word, path):
        pass

    @abstractmethod
    def delete_vacancies(self, filter_word, path):
        pass


class JSONSaver(ABCSaver):
    """Отвечает за сохранение, получение, удаление и поиск в файле json"""
    def write(self, data: dict, filename: str):
        """Метод записи данных в json"""
        with open(filename, 'r', encoding='UTF-8') as file:
            old_data = json.load(file)
        for i in data['items']:
            old_data['items'].append(i)
        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(old_data, file, indent=4, ensure_ascii=False)

    def read(self, filename: str) -> dict:
        """Выводит информацию о вакансиях из файла"""
        with open(filename, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        return data

    def clear(self, filename: str):
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
            self.write(vacancy, filename)
            vacansy = self.read(filename)['items']
            for i in vacansy:
                filtered_vacancies.append(i)
        elif user_platform == '2':
            vacancy = SuperJob().get_requests(filter_word)
            self.write(vacancy, filename)
            vacansy = self.read(filename)['items']
            for i in vacansy:
                filtered_vacancies.append(i)
        elif user_platform == '3':
            vacancy = HeadHunter().get_requests(filter_word)
            self.write(vacancy, filename)
            vacancy = SuperJob().get_requests(filter_word)
            self.write(vacancy, filename)
            vacansy = self.read(filename)['items']
            for i in vacansy:
                filtered_vacancies.append(i)
        elif user_platform == '0':
            vacansy = self.read(filename)['items']
            for i in vacansy:
                if filter_word.lower() in str(i['name']).lower():
                    filtered_vacancies.append(i)
        else:
            print('Что-то пошло не так')
        return filtered_vacancies

    def delete_vacancies(self, filter_word, filename):
        count_deleted_vacancies = 0
        filtered_vacancies = {}
        filtered_vacancies = {'items': []}
        vacansy = self.read(filename)['items']
        for i in vacansy:
            if filter_word.lower() not in str(i['name']).lower():
                filtered_vacancies['items'].append(i)
            else:
                count_deleted_vacancies += 1
        self.clear(filename)
        self.write(filtered_vacancies, filename)
        return count_deleted_vacancies


