from SbisPages import SearchHelper

def testing(browser):
  global script_1
  script_1 = SearchHelper(browser)
    
def test_start():
  script_1.start()
  
def test_click_picture():
  script_1.click_picture()

def test_switch_window():
  script_1.switch_window()
  
def test_check_block():
  script_1.check_block()

def test_detail_link():
  script_1.detail_link()

def test_detail_click():
  script_1.detail_click()

def test_detail_link_2():
  script_1.detail_link_2()
    
def test_check_pictures():
  script_1.check_pictures()

def test_report():
  script_1.report()