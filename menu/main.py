
#from Utils.Vacansy import Vacancy
from Utils.API_Classes import HeadHunter
#from Utils.utils import is_empty_file

print('Привет!')

if is_empty_file() == False:
    is_work_withs_file = input('Уже есть загруженные данные. Использовать их?\n1 - Да\n2 - Нет, хочу загрузить новые\n')
else:
    is_work_withs_file = '2'

if is_work_withs_file == '2':
    choise_platform = input('С какой платформы хочешь получить данные?\n1 - hh.ru\n2 - SuperJob.ru\n3 - С обеих сразу\n')


vacancy = HeadHunter().get_requests()
#write_to_json(vacancy)


