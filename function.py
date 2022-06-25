def rename_function(func_name):
    print(func_name.replace('_',' ').capitalize())
    pass

def open_browser(browser_name):
    rename_function(open_browser.__name__)
    pass


def go_to_companyname_homepage(page_url):
    rename_function(go_to_companyname_homepage.__name__)
    pass


def find_registration_button_on_login_page(page_url, button_text):
    rename_function(find_registration_button_on_login_page.__name__)
    pass

open_browser('')
go_to_companyname_homepage('')
find_registration_button_on_login_page('', '')