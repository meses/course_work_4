
from Utils.Vacansy import Vacancy, top_vacancies, show_vacancies
#from Utils.API_Classes import HeadHunter, SuperJob
from Utils.utils import file_or_new_request, clear_json, get_filtered_vacancies, is_get_top, how_mutch_vacansies_show

filename = '../Utils/data.json'

def main():
    print('Привет!')

    user_platform = file_or_new_request(filename)
    filter_word = input(f'Введите название вакансии для поиска: ')

    if user_platform != '0':
        clear_json(filename)

    filtered_vacancies = get_filtered_vacancies(user_platform, filter_word, filename)

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

    print('Спасибо, приходите ещё!')

if __name__=="__main__":
    main()


