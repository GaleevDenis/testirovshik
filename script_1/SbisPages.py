import time
from BaseApp import BasePage
from selenium.webdriver.common.by import By

class SbisSeacrhLocators:

    LOCATOR_SBIS_CLICK_PICTURE = (By.CSS_SELECTOR, "div [href='https://tensor.ru/'] img")
    LOCATOR_SBIS_CLOSE_FIND_WINDOW_1 = (By.CSS_SELECTOR, ".sbis_ru-CookieAgreement.ws-hidden")
    LOCATOR_SBIS_CLOSE_WINDOW_1 = (By.CSS_SELECTOR, ".sbis_ru-CookieAgreement__close")
    LOCATOR_SBIS_CLOSE_FIND_WINDOW = (By.CSS_SELECTOR, ".tensor_ru-CookieAgreement.ws-flexbox.ws-justify-content-between.ws-hidden")
    LOCATOR_SBIS_CLOSE_WINDOW = (By.CSS_SELECTOR, ".tensor_ru-CookieAgreement__close.icon-Close.ws-flex-shrink-0.ws-flexbox.ws-align-items-center")
    LOCATOR_SBIS_CHECK_BLOCK = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content.tensor_ru-Index__card.tensor_ru-Index__block4-content.tensor_ru-Index__card")
    LOCATOR_SBIS_DETAIL_LINK = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content.tensor_ru-Index__card .tensor_ru-Index__card-text:nth-child(4) [href='/about']")
    LOCATOR_SBIS_DETAIL_LINK_2 = (By.XPATH, "//meta[@content='https://tensor.ru/about']")
    LOCATOR_SBIS_DETAIL_CLICK = (By.CSS_SELECTOR, "[href='/about'].tensor_ru-link.tensor_ru-Index__link")
    LOCATOR_SBIS_CHECK_PICTURES = (By.CSS_SELECTOR, ".tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 img")
    LOCATOR_SBIS_CHECK_WIDTH = ("width")
    LOCATOR_SBIS_CHECK_HEIGHT = ("height")


class SearchHelper(BasePage):

    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        temp_1 = self.base_url
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            print('-------------------------Отчет-------------------------\n', file=file_out)
            if temp_1 == "https://sbis.ru/contacts":
                text_1 = "1.  Переход на сайт."
                print(text_1)
                print(text_1, file=file_out)
                assert temp_1 == "https://sbis.ru/contacts"
            else:
                text_1 = "1.  Ошибка, переход на сайт 'https://sbis.ru/contacts' не выполнен."             
                print(text_1)
                print(text_1, file=file_out)
                assert temp_1 == "https://sbis.ru/contacts", "1.  Ошибка, переход на сайт 'https://sbis.ru/contacts' не выполнен."

    def click_picture(self):
        time.sleep(3)
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            try:
                self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_FIND_WINDOW_1)
            except:
                self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_WINDOW_1).click()
                try:
                    temp_2 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CLICK_PICTURE)
                except:
                    text_2 = "2.  Ошибка, баннер 'Тензор' отсутствует, переход невозможен."
                    print(text_2)
                    print(text_2, file=file_out)
                    assert temp_2 != False, "2.  Ошибка, баннер 'Тензор' отсутствует, переход невозможен."
                else:
                    try:
                        temp_2 = self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CLICK_PICTURE).click()
                    except:
                        text_2 = "2.  Ошибка, баннер 'Тензор' найден, клик не удался."
                        print(text_2)
                        print(text_2, file=file_out)
                        assert temp_2 != False, "2.  Ошибка, баннер 'Тензор' найден, клик не удался."           
                    else:
                        text_2 = "2.  Баннер 'Тензор' сушествует, осуществляется переход."
                        print(text_2)
                        print(text_2, file=file_out)
                        assert temp_2 != False
            else:
                try:
                    temp_2 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CLICK_PICTURE)
                except:
                    text_2 = "2.  Ошибка, баннер 'Тензор' отсутствует, переход невозможен."
                    print(text_2)
                    print(text_2, file=file_out)
                    assert temp_2 != False, "2.  Ошибка, баннер 'Тензор' отсутствует, переход невозможен."
                else:
                    try:
                        temp_2 = self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CLICK_PICTURE).click()
                    except:
                        text_2 = "2.  Ошибка, баннер 'Тензор' найден, клик не удался."
                        print(text_2)
                        print(text_2, file=file_out)
                        assert temp_2 != False, "2.  Ошибка, баннер 'Тензор' найден, клик не удался."           
                    else:
                        text_2 = "2.  Баннер 'Тензор' сушествует, осуществляется переход."
                        print(text_2)
                        print(text_2, file=file_out)
                        assert temp_2 != False

    def switch_window(self):
        time.sleep(3)
        lists = []
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            for handle in self.driver.window_handles:
                lists.append(handle)
            try :
                self.driver.switch_to.window(lists[1])
            except:
                text_3 = "3.  Ошибка, перехода на второе окно."
                print(text_3)
                print(text_3, file=file_out)  
                assert text_3 == False, "3.  Ошибка, перехода на второе окно."
            else:
                text_3 = "3.  Переход на второе окно."              
                print(text_3)
                print(text_3, file=file_out)
                assert type(text_3) == str

    def check_block(self):
        self.driver.refresh()
        time.sleep(3)
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            try: 
                self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_FIND_WINDOW)
            except:
                self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_WINDOW).click()
                try: 
                    temp_4 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_BLOCK)
                except:
                    text_4 = "4.  Ошибка, блок 'Сила в людях' не найден."
                    print(text_4)
                    print(text_4, file=file_out)
                    assert temp_4 != False, "4.  Ошибка, блок 'Сила в людях' не найден."
                else:
                    text_4 = "4.  Проверка, есть блок 'Сила в людях'."
                    print(text_4)
                    print(text_4, file=file_out)
                    assert temp_4 != False
            else:
                try: 
                    temp_4 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_BLOCK)
                except:
                    text_4 = "4.  Ошибка, блок 'Сила в людях' не найден."
                    print(text_4)
                    print(text_4, file=file_out)
                    assert temp_4 != False, "4.  Ошибка, блок 'Сила в людях' не найден."
                else:
                    text_4 = "4.  Проверка, есть блок 'Сила в людях'."
                    print(text_4)
                    print(text_4, file=file_out)
                    assert temp_4 != False

    def detail_link(self):
        time.sleep(3)
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            try:
                temp_5 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_DETAIL_LINK)
            except:
                text_5 = "5.  Ошибка, перейдет не на 'https://tensor.ru/about'."
                print(text_5)
                print(text_5, file=file_out)
                assert temp_5 != False, "5.  Ошибка, перейдет не на 'https://tensor.ru/about'."
            else:
                text_5 = "5.  Проверка, откроется 'https://tensor.ru/about'."
                print(text_5)
                print(text_5, file=file_out)
                assert temp_5 != False
    
    def detail_click(self):
        time.sleep(3)
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            try: 
                self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_FIND_WINDOW)
            except:
                self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_WINDOW).click()
                try: 
                    temp_6 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_DETAIL_CLICK)
                except:
                    text_6 = "5.1 Ошибка, кнопка 'Подробнее' отсутствует, переход невозможен."
                    print(text_6)
                    print(text_6, file=file_out)
                    assert temp_6 != False, "5.1 Ошибка, кнопка 'Подробнее' отсутствует, переход невозможен."
                else:
                    try:
                        self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_DETAIL_CLICK).click()
                    except:
                        text_6 = "5.1 Ошибка, кнопка 'Подробнее' найдена, переход неудался."
                        print(text_6)
                        print(text_6, file=file_out)
                        assert temp_6 != False, "5.1 Ошибка, кнопка 'Подробнее' найдена, переход неудался."          
                    else:
                        text_6 = "5.1 Осуществляется переход по кнопке 'Подробнее'."
                        print(text_6)
                        print(text_6, file=file_out)
                        assert temp_6 != False       
            else:
                try: 
                    temp_6 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_DETAIL_CLICK)
                except:
                    text_6 = "5.1 Ошибка, кнопка 'Подробнее' отсутствует, переход невозможен."
                    print(text_6)
                    print(text_6, file=file_out)
                    assert temp_6 != False, "5.1 Ошибка, кнопка 'Подробнее' отсутствует, переход невозможен."
                else:
                    try:
                        self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_DETAIL_CLICK).click()
                    except:
                        text_6 = "5.1 Ошибка, кнопка 'Подробнее' найдена, переход неудался."
                        print(text_6)
                        print(text_6, file=file_out)
                        assert temp_6 != False, "5.1 Ошибка, кнопка 'Подробнее' найдена, переход неудался."          
                    else:
                        text_6 = "5.1 Осуществляется переход по кнопке 'Подробнее'."
                        print(text_6)
                        print(text_6, file=file_out)
                        assert temp_6 != False         

    def detail_link_2(self):
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            time.sleep(3)
            try:
                temp_7 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_DETAIL_LINK_2)
            except:
                text_7 = "5.2 Ошибка, переход не на 'https://tensor.ru/about'."
                print(text_7)
                print(text_7, file=file_out)
                assert temp_7 != False, "5.2 Ошибка, переход не на 'https://tensor.ru/about'."
            else:
                text_7 = "5.2 Проверка, открылась 'https://tensor.ru/about'."
                print(text_7)
                print(text_7, file=file_out)
                assert temp_7 != False
    
    def check_pictures(self):
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            time.sleep(3)
            try: 
                self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_FIND_WINDOW)
            except:
                self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_WINDOW).click()
                try:
                    pictures = self.find_elements(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_PICTURES)
                except:
                    text_8 = "6.  Ошибка, фотографии не найдены."
                    print(text_8)
                    print(text_8, file=file_out)
                    assert pictures != False, "6.  Ошибка, фотографии не найдены."               
                else:
                    width_start = pictures[0].get_attribute(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_WIDTH)
                    height_start = pictures[0].get_attribute(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_HEIGHT)
                    temp_8 = 0
                    for i in range(len(pictures)):
                        width = pictures[i].get_attribute(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_WIDTH)
                        height = pictures[i].get_attribute(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_HEIGHT)
                        if (width == width_start) and (height == height_start):
                            temp_8 += 1
                    if temp_8 == len(pictures):
                        text_8 = "6.  Проверка, у всех фотографий одинаковые высота и ширина."
                        print(text_8)
                        print(text_8, file=file_out)
                        assert temp_8 == len(pictures)
                    else:
                        text_8 = "6.  Проверка, у фотографий разные высота и ширина."
                        print(text_8)
                        print(text_8, file=file_out)
                        assert temp_8 == len(pictures), "6.  Проверка, у фотографий разные высота и ширина."
            else:
                try:
                    pictures = self.find_elements(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_PICTURES)
                except:
                    text_8 = "6.  Ошибка, фотографии не найдены."
                    print(text_8)
                    print(text_8, file=file_out)
                    assert pictures != False, "6.  Ошибка, фотографии не найдены."               
                else:
                    width_start = pictures[0].get_attribute(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_WIDTH)
                    height_start = pictures[0].get_attribute(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_HEIGHT)
                    temp_8 = 0
                    for i in range(len(pictures)):
                        width = pictures[i].get_attribute(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_WIDTH)
                        height = pictures[i].get_attribute(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_HEIGHT)
                        if (width == width_start) and (height == height_start):
                            temp_8 += 1
                    if temp_8 == len(pictures):
                        text_8 = "6.  Проверка, у всех фотографий одинаковые высота и ширина."
                        print(text_8)
                        print(text_8, file=file_out)
                        assert temp_8 == len(pictures)
                    else:
                        text_8 = "6.  Проверка, у фотографий разные высота и ширина."
                        print(text_8)
                        print(text_8, file=file_out)
                        assert temp_8 == len(pictures), "6.  Проверка, у фотографий разные высота и ширина."

    def report(self):
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            text_9 = "7.  Сформирован отчет в документе 'report.txt'"
            print(text_9 + "\n\n\n", file=file_out)
            print(text_9)
