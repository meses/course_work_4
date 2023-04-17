from classes.vacansy_class import Vacancy, top_vacancies, show_vacancies
from utils.utils import file_or_new_request,  is_get_top, how_mutch_vacansies_show
from classes.local_file_class import JSONSaver
import os

filename = 'utils/data.json'
key = os.getenv("SUPERJOB_KEY")

if key is None:
    print('Для работы нужен ключ SUPERJOB_KEY в переменных окружения')
    quit()

def main():
    print('Привет!')

    user_platform = file_or_new_request(filename)
    filter_word = input(f'Введите название вакансии для поиска: ')

    if user_platform != '0':
        JSONSaver().clear(filename)

    filtered_vacancies = JSONSaver().get_filtered_vacancies(user_platform, filter_word, filename)

    if len(filtered_vacancies) == 0:
        print('По вашему запросу ничего не нашлось')
    else:
        vac_objs = [Vacancy(i['name'], i['salary'], i['company_name'], i['url']) for i in
                    filtered_vacancies]  # Создаёт экземпляры класса Vacancy из всего списка вакансий, полученных из файла
        print(f'Всего вакансий нашлось: {len(vac_objs)}')
        is_top = is_get_top()
        if is_top == '1':
            count_vacancies = how_mutch_vacansies_show()
            top = top_vacancies(vac_objs, count_vacancies)
            show_vacancies(top)

        elif is_top == '2':
            is_all_vacancies = input(f'Тогда может вывести все найденные вакансии?\n1 - Да\n2 - Нет\n')
            if is_all_vacancies == '1':
                show_vacancies(vac_objs)


    is_delete = input('Хотите удалить вакансии?\n1 - Да\n2 - Нет\n')
    if is_delete == '1':
        filter_word = input('Введите название вакансии для удаления: ')
        deleted_vacancies = JSONSaver().delete_vacancies(filter_word, filename)
        print(f'Удалено {deleted_vacancies} вакансий')

    print('\nСпасибо, приходите ещё!')

if __name__=="__main__":
    main()


