import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',  #english - язык по умолчанию
                     help="Choose language")



@pytest.fixture(scope="function") #функция выбора браузера
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
       print("\nstart firefox browser for test..")
       fp = webdriver.FirefoxProfile()
       fp.set_preference("intl.accept_languages", user_language)
       browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print(f"{browser_name} wasn't implemented")
       #raise pytest.UsageError("please choose the language")
    yield browser
    print("\nquit browser..")
    browser.quit()