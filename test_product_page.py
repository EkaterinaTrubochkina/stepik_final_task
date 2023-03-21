import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time
#from .pages.basket_page import BasketPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    time.sleep(10)
    page.should_be_added_to_basket() 
    time.sleep(10)
    