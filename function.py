# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__


def name_function(func_name):
    function_name = func_name.__name__.replace('_',' ').capitalize()
    function_arguments = func_name.__code__.co_varnames
    arguments_name = list(function_arguments if len(function_arguments) != 0 else ['Аргументы отсутствуют'])
    arguments_name = [arg.replace('_',' ').capitalize() for arg in arguments_name]
    print(f'Название функции: {function_name}. Аргументы функции: {", ".join(arguments_name)}')
    pass

def open_browser(browser_name):
    name_function(open_browser)
    pass


def go_to_companyname_homepage(page_url):
    name_function(go_to_companyname_homepage)
    pass


def find_registration_button_on_login_page(page_url, button_text):
    name_function(find_registration_button_on_login_page)
    pass

def function_without_arguments():
    name_function(function_without_arguments)
    pass

open_browser('')
go_to_companyname_homepage('')
find_registration_button_on_login_page('', '')
function_without_arguments()