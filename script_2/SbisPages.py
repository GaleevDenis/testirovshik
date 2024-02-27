import time
from BaseApp import BasePage
from selenium.webdriver.common.by import By

class SbisSeacrhLocators:

    LOCATOR_SBIS_CLOSE_FIND_WINDOW = (By.CSS_SELECTOR, ".sbis_ru-CookieAgreement.ws-hidden")
    LOCATOR_SBIS_CLOSE_WINDOW = (By.CSS_SELECTOR, ".sbis_ru-CookieAgreement__close")
    LOCATOR_SBIS_DETAIL_REGION = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text.sbis_ru-link")
    LOCATOR_SBIS_CHECK_BLOCK_REGION = (By.CSS_SELECTOR, ".sbisru-Contacts-List__col.ws-flex-shrink-1.ws-flex-grow-1  \
                                       div[name='itemsContainer'][data-qa='items-container']")
    LOCATOR_SBIS_CHECK_BLOCK_PARTNERS = (By.CSS_SELECTOR, ".sbisru-Contacts-List__col.ws-flex-shrink-1.ws-flex-grow-1  \
                                         div[name='itemsContainer'][data-qa='items-container'] div[data-qa='item']")
    LOCATOR_SBIS_CHANGE_REGION = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser.ml-16.ml-xm-0 .sbis_ru-Region-Chooser__text.sbis_ru-link")
    LOCATOR_SBIS_CHANGE_REGION_CLICK = (By.CSS_SELECTOR, "span[title='Камчатский край']")
    LOCATOR_SBIS_CHECK_URL_REGION = (By.XPATH, "//meta[@sid='h-ps-16']")
    LOCATOR_SBIS_CHECK_TITLE_REGION = (By.XPATH, "//meta[@sid='h-ps-17']")


class SearchHelper(BasePage):
    
    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        temp_1 = self.base_url
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            print('-----------------------------------Отчет-----------------------------------\n', file=file_out)
            if temp_1 == "https://sbis.ru/contacts":
                assert temp_1 == "https://sbis.ru/contacts"
                text_1 = "1.   Переход на сайт 'https://sbis.ru/contacts'."
                print(text_1, file=file_out)
                print(text_1)
            else:
                text_1 = "1.   Ошибка, переход на сайт 'https://sbis.ru/contacts' не выполнен."
                print(text_1, file=file_out)
                print(text_1)
                assert temp_1 == "https://sbis.ru/contacts", "1.   Ошибка, переход на сайт 'https://sbis.ru/contacts' не выполнен."
    
    def detail_region(self):
        time.sleep(3)
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            try:
                self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_FIND_WINDOW)
            except:
                self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_WINDOW).click()
                try:
                    temp_2 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_DETAIL_REGION).text.find("Республика Башкортостан")
                except:
                    text_2 = "2.   Ошибка, элемент 'регион' не был найден"
                    print(text_2, file=file_out)
                    print(text_2)
                    assert temp_2 != False, "2.   Ошибка, элемент 'регион' не был найден"
                else:
                    if temp_2 != -1:
                        assert temp_2 != -1
                        text_2 = "2.   Регион 'Республика Башкортостан' определился."
                        print(text_2, file=file_out)
                        print(text_2)
                    else:
                        text_2 = "2.  Ошибка, регион 'Республика Башкортостан' не определился."
                        print(text_2, file=file_out)
                        print(text_2)
                        assert temp_2 != -1, "2.  Ошибка, регион 'Республика Башкортостан' не определился."
            else:
                try:
                    temp_2 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_DETAIL_REGION).text.find("Республика Башкортостан")
                except:
                    text_2 = "2.   Ошибка, элемент 'регион' не был найден"
                    print(text_2, file=file_out)
                    print(text_2)
                    assert temp_2 != False, "2.   Ошибка, элемент 'регион' не был найден"
                else:
                    if temp_2 != -1:
                        assert temp_2 != -1
                        text_2 = "2.   Регион 'Республика Башкортостан' определился."
                        print(text_2, file=file_out)
                        print(text_2)
                    else:
                        text_2 = "2.  Ошибка, регион 'Республика Башкортостан' не определился."
                        print(text_2, file=file_out)
                        print(text_2)
                        assert temp_2 != -1, "2.  Ошибка, регион 'Республика Башкортостан' не определился."
            
    def check_block_region(self):
        time.sleep(3)
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            try: 
                self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_FIND_WINDOW)
            except:
                self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_WINDOW).click()
                try: 
                    temp_3 = self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_BLOCK_REGION)
                except:
                    text_3 = "2.1  Ошибка, блок 'Список партнеров' отсутствует."
                    print(text_3, file=file_out)
                    print(text_3)
                    assert temp_3 != False, "2.1  Ошибка, блок 'Список партнеров' отсутствует."
                else:
                    try:
                        self.partners = self.find_elements(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_BLOCK_PARTNERS)
                    except:
                        text_3 = "2.1  Ошибка, блок 'Список партнеров' сушествует, текущий список партнеров не сохранен(найден)."
                        print(text_3, file=file_out)
                        print(text_3)
                        assert self.partners != False, "2.1  Ошибка, блок 'Список партнеров' сушествует, текущий список партнеров не сохранен(найден)."
                    else:
                        assert self.partners != False
                        text_3 = "2.1  Блок 'Список партнеров' сушествует, текущий список партнеров сохранен."
                        print(text_3, file=file_out)
                        print(text_3) 
            else:
                try: 
                    temp_3 = self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_BLOCK_REGION)
                except:
                    text_3 = "2.1  Ошибка, блок 'Список партнеров' отсутствует."
                    print(text_3, file=file_out)
                    print(text_3)
                    assert temp_3 != False, "2.1  Ошибка блок 'Список партнеров' отсутствует."
                else:
                    try:
                        self.partners = self.find_elements(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_BLOCK_PARTNERS)
                    except:
                        text_3 = "2.1  Ошибка, блок 'Список партнеров' сушествует, текущий список партнеров не сохранен(найден)."
                        print(text_3, file=file_out)
                        print(text_3)
                        assert self.partners != False, "2.1  Ошибка, блок 'Список партнеров' сушествует, текущий список партнеров не сохранен(найден)."
                    else:
                        assert self.partners != False
                        text_3 = "2.1  Блок 'Список партнеров' сушествует, текущий список партнеров сохранен."
                        print(text_3, file=file_out)
                        print(text_3)

    def change_region(self):
        time.sleep(3)
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            try:
                self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_FIND_WINDOW)
            except:
                self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_WINDOW).click()
                try:
                    temp_4 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CHANGE_REGION)
                except:
                    text_4 = "3.   Ошибка, строка смены региона не найдена, переход невозможен."
                    print(text_4, file=file_out)
                    print(text_4)
                    assert temp_4 != False, "3.   Ошибка, строка смены региона не найдена, переход невозможен."
                else:
                    self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CHANGE_REGION).click()
                    assert temp_4 != False
                    text_4 = "3.   Переход в окно смены региона."
                    print(text_4, file=file_out)
                    print(text_4)
            else:
                try:
                    temp_4 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CHANGE_REGION)
                except:
                    text_4 = "3.   Ошибка, строка смены региона не найдена, переход невозможен."
                    print(text_4, file=file_out)
                    print(text_4)
                    assert temp_4 != False, "3.   Ошибка, строка смены региона не найдена, переход невозможен."
                else:
                    self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CHANGE_REGION).click()
                    assert temp_4 != False
                    text_4 = "3.   Переход в окно смены региона."
                    print(text_4, file=file_out)
                    print(text_4)          
            
    def change_region_click(self):
        time.sleep(3)
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            try: 
                self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_FIND_WINDOW)
            except:
                self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_WINDOW).click()
                try: 
                    temp_5 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CHANGE_REGION_CLICK)
                except:
                    text_5 = "3.1  Ошибка, не найден элемент 'Камчатский край', код региона не сохранен."
                    print(text_5, file=file_out)
                    print(text_5)
                    assert temp_5 != False, "3.1  Ошибка, не найден элемент 'Камчатский край', код региона не сохранен."
                else:
                    try:
                        self.kod_region = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CHANGE_REGION_CLICK).text[0:2]
                    except:
                        text_5 = "3.1  Ошибка, код региона не найден."
                        print(text_5, file=file_out)
                        print(text_5)
                        assert self.kod_region != False, "3.1  Ошибка, код региона не найден."
                    else:
                        try:
                            temp_5 = self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CHANGE_REGION_CLICK).click()
                        except:
                            text_5 = "3.1 Ошибка, смены региона на 'Камчатский край', код региона найден."
                            print(text_5, file=file_out)
                            print(text_5)
                            assert temp_5 != False, "3.1 Ошибка, смены региона на 'Камчатский край', код региона найден."                 
                        else:   
                            text_5 = "3.1  Смена региона на 'Камчатский край', код региона сохранен."
                            print(text_5, file=file_out)
                            print(text_5)
                            assert temp_5 != False
            else:                      
                try: 
                    temp_5 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CHANGE_REGION_CLICK)
                except:
                    text_5 = "3.1  Ошибка, не найден элемент 'Камчатский край', код региона не сохранен."
                    print(text_5, file=file_out)
                    print(text_5)
                    assert temp_5 != False, "3.1  Ошибка, не найден элемент 'Камчатский край', код региона не сохранен."
                else:
                    try:
                        self.kod_region = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CHANGE_REGION_CLICK).text[0:2]
                    except:
                        text_5 = "3.1  Ошибка, код региона не найден."
                        print(text_5, file=file_out)
                        print(text_5)
                        assert self.kod_region != False, "3.1  Ошибка, код региона не найден."
                    else:
                        try:
                            temp_5 = self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CHANGE_REGION_CLICK).click()
                        except:
                            text_5 = "3.1 Ошибка, смены региона на 'Камчатский край', код региона найден."
                            print(text_5, file=file_out)
                            print(text_5)
                            assert temp_5 != False, "3.1 Ошибка, смены региона на 'Камчатский край', код региона найден."                 
                        else:   
                            text_5 = "3.1  Смена региона на 'Камчатский край', код региона сохранен."
                            print(text_5, file=file_out)
                            print(text_5)
                            assert temp_5 != False
                    
    def detail_region_2(self): 
        time.sleep(3)
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            try:
                self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_FIND_WINDOW)
            except:
                self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_WINDOW).click()
                try:
                    temp_6 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_DETAIL_REGION).text.find("Камчатский край")
                except:
                    text_6 = "4.   Ошибка, элемент 'регион' не был найден"
                    print(text_6, file=file_out)
                    print(text_6)
                    assert temp_6 != -1, "4.   Ошибка, элемент 'регион' не был найден" 
                else:
                    if temp_6 != -1:
                        assert temp_6 != -1
                        text_6 = "4.   Проверка, регион изменился на 'Камчатский край'."
                        print(text_6, file=file_out)
                        print(text_6)
                    else:
                        text_6 = "4.   Ошибка, регион не изменился на 'Камчатский край'."
                        print(text_6, file=file_out)
                        print(text_6)
                        assert temp_6 != -1, "4.   Ошибка, регион не изменился на 'Камчатский край'."
            else:
                try:
                    temp_6 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_DETAIL_REGION).text.find("Камчатский край")
                except:
                    text_6 = "4.   Ошибка, элемент 'регион' не был найден"
                    print(text_6, file=file_out)
                    print(text_6)
                    assert temp_6 != -1, "4.   Ошибка, элемент 'регион' не был найден" 
                else:
                    if temp_6 != -1:
                        assert temp_6 != -1
                        text_6 = "4.   Проверка, регион изменился на 'Камчатский край'."
                        print(text_6, file=file_out)
                        print(text_6)
                    else:
                        text_6 = "4.   Ошибка, регион не изменился на 'Камчатский край'."
                        print(text_6, file=file_out)
                        print(text_6)
                        assert temp_6 != -1, "4.   Ошибка, регион не изменился на 'Камчатский край'."

    def check_block_region_2(self):
        time.sleep(3)
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            try: 
                self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_FIND_WINDOW)
            except:
                self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_WINDOW).click()
                try: 
                    temp_7 = self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_BLOCK_REGION)
                except:
                    text_7 = "4.1  Ошибка, блок 'Список партнеров' отсутствует."
                    print(text_7, file=file_out)
                    print(text_7)
                    assert temp_7 != False, "4.1  Ошибка, блок 'Список партнеров' отсутствует."  
                else:
                    self.partners_2 = self.find_elements(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_BLOCK_PARTNERS)
                    if (self.partners_2 != self.partners) and (self.partners != False) and (self.partners_2 != False):
                        assert self.partners_2 != self.partners
                        text_7 = "4.1  Проверка, список партнеров изменился."
                        print(text_7, file=file_out)
                        print(text_7)
                    else:
                        text_7 = "4.1  Ошибка, список партнеров не изменился."
                        print(text_7, file=file_out)
                        print(text_7)
                        assert self.partners_2 == "True", "4.1  Ошибка, список партнеров не изменился."
            else:
                try: 
                    temp_7 = self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_BLOCK_REGION)
                except:
                    text_7 = "4.1  Ошибка, блок 'Список партнеров' отсутствует."
                    print(text_7, file=file_out)
                    print(text_7)
                    assert temp_7 != False, "4.1  Ошибка, блок 'Список партнеров' отсутствует."  
                else:
                    self.partners_2 = self.find_elements(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_BLOCK_PARTNERS)
                    if (self.partners_2 != self.partners) and (self.partners != False) and (self.partners_2 != False):
                        assert self.partners_2 != self.partners
                        text_7 = "4.1  Проверка, список партнеров изменился."
                        print(text_7, file=file_out)
                        print(text_7)
                    else:
                        text_7 = "4.1  Ошибка, список партнеров не изменился."
                        print(text_7, file=file_out)
                        print(text_7)
                        assert self.partners_2 == "True", "4.1  Ошибка, список партнеров не изменился."
                       
    def check_url_region_2(self): 
        self.driver.refresh()
        time.sleep(5)
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            try:
                self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_FIND_WINDOW)
            except:
                self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_WINDOW).click()
                try:
                    temp_8 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_URL_REGION).get_attribute("content")
                except:
                    text_8 = "4.2  Ошибка, URL не был найден."
                    print(text_8, file=file_out)
                    print(text_8)
                    assert temp_8 != False, "4.2  Ошибка, URL не был найден."
                else:
                    if temp_8.find(self.kod_region) != -1:
                        assert temp_8.find(self.kod_region) != -1
                        text_8 = "4.2  Проверка, URL соответствует выбраному региону."
                        print(text_8, file=file_out)
                        print(text_8)
                    else:
                        text_8 = "4.2  Ошибка, URL не соответствует выбраному региону."
                        print(text_8, file=file_out)
                        print(text_8)
                        assert temp_8.find(self.kod_region) != -1, "4.2  Ошибка, URL не соответствует выбраному региону."
            else:
                try:
                    temp_8 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_URL_REGION).get_attribute("content")
                except:
                    text_8 = "4.2  Ошибка, URL не был найден."
                    print(text_8, file=file_out)
                    print(text_8)
                    assert temp_8 != False, "4.2  Ошибка, URL не был найден."
                else:
                    if temp_8.find(self.kod_region) != -1:
                        assert temp_8.find(self.kod_region) != -1
                        text_8 = "4.2  Проверка, URL соответствует выбраному региону."
                        print(text_8, file=file_out)
                        print(text_8)
                    else:
                        text_8 = "4.2  Ошибка, URL не соответствует выбраному региону."
                        print(text_8, file=file_out)
                        print(text_8)
                        assert temp_8.find(self.kod_region) != -1, "4.2  Ошибка, URL не соответствует выбраному региону."
                   
    def check_title_region_2(self): 
        self.driver.refresh()
        time.sleep(5)
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            try:
                self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_FIND_WINDOW)
            except:
                self.check_click(SbisSeacrhLocators.LOCATOR_SBIS_CLOSE_WINDOW).click()
                try:
                    temp_9 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_TITLE_REGION).get_attribute("content")\
                        .find(self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_DETAIL_REGION).text[:-1])
                except:
                    text_9 = "4.3  Ошибка, title не был найден."
                    print(text_9, file=file_out)
                    print(text_9)
                    assert temp_9 != -1, "4.3  Ошибка, title не был найден."
                else:
                    if temp_9 != -1:
                        assert temp_9 != -1
                        text_9 = "4.3  Проверка, title содержит информацию о выбраном регионе."
                        print(text_9, file=file_out)
                        print(text_9)
                    else:
                        text_9 = "4.3  Ошибка, title не содержит информацию о выбраном регионе."
                        print(text_9, file=file_out)
                        print(text_9)
                        assert temp_9 != -1, "4.3  Ошибка, title не содержит информацию о выбраном регионе."
            else:
                try:
                    temp_9 = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_CHECK_TITLE_REGION).get_attribute("content")\
                        .find(self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_DETAIL_REGION).text[:-1])
                except:
                    text_9 = "4.3  Ошибка, title не был найден."
                    print(text_9, file=file_out)
                    print(text_9)
                    assert temp_9 != -1, "4.3  Ошибка, title не был найден."
                else:
                    if temp_9 != -1:
                        assert temp_9 != -1
                        text_9 = "4.3  Проверка, title содержит информацию о выбраном регионе."
                        print(text_9, file=file_out)
                        print(text_9)
                    else:
                        text_9 = "4.3  Ошибка, title не содержит информацию о выбраном регионе."
                        print(text_9, file=file_out)
                        print(text_9)
                        assert temp_9 != -1, "4.3  Ошибка, title не содержит информацию о выбраном регионе."
                        
    def report(self):
        with open(file="report.txt", mode="a+", encoding="UTF-8") as file_out:
            text_10 = "5.   Сформирован отчет в документе 'report.txt'"
            print(text_10 + "\n\n\n", file=file_out)
            print(text_10)