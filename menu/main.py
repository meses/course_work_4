
from Utils.Vacansy import Vacancy, top_vacancies, show_vacancies
from Utils.API_Classes import HeadHunter
from Utils.utils import is_empty_file, select_services, file_or_new_request, get_info_from_json, write_to_json, clear_json

filename = '../Utils/data.json'
print('Привет!')

user_platform = file_or_new_request(filename)
filter_word = input(f'Введите название вакансии для поиска: ')

if user_platform != '0':
    clear_json(filename)

filtered_vacancies = []
if user_platform == '1':
    vacancy = HeadHunter().get_requests(filter_word)
    write_to_json(vacancy, filename)
    vacansy = get_info_from_json(filename)['items']
    for i in vacansy:
        filtered_vacancies.append(i)
elif user_platform == '2':
    pass
elif user_platform == '3':
    pass
elif user_platform == '0':
    vacansy = get_info_from_json(filename)['items']
    for i in vacansy:
        if filter_word.lower() in str(i['name']).lower():
            filtered_vacancies.append(i)
else:
    print('Что-то пошло не так')
#vacancy = HeadHunter().get_requests('Руководитель')
#write_to_json(vacancy, filename)



vac_objs = [Vacancy(i['name'], i['salary'], i['company_name'], i['url']) for i in filtered_vacancies] # Создаёт экземпляры класса Vacancy из всего списка вакансий, полученных из файла
#vac_objs.sort(key=lambda x: x.salary['from'])
#print(vac_objs[:5])
is_top = input('Вывести топ вакансий по зарплате?\n1 - Да\n2 - Нет\n')
if is_top == '1':
    print(f'Всего вакансий нашлось: {len(vac_objs)}')
    count_vacancies = int(input('Сколько вакансий показать? '))
    top_vacancies = top_vacancies(vac_objs, count_vacancies)
    show_vacancies(top_vacancies)

elif is_top == '2':
    is_all_vacancies = input(f'Тогда может вывести все найденные вакансии? Их нашлось: {len(vac_objs)}\n1 - Да\n2 - Нет\n')
    if is_all_vacancies == '1':
        show_vacancies(vac_objs)
# print(len(vac_objs))
#vac_objs.sort(key=lambda x: x.salary['to'])
#print(top_vacancies(vac_objs, 5))



