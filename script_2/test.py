from SbisPages import SearchHelper

def testing(browser):
  global script_1
  script_1 = SearchHelper(browser)
    
def test_start():
  script_1.start()

def test_detail_region():
  script_1.detail_region()

def test_check_block_region():
  script_1.check_block_region()

def test_change_region():
  script_1.change_region()

def test_change_region_click():
  script_1.change_region_click()

def test_detail_region_2():
  script_1.detail_region_2()
   
def test_check_block_region_2():
  script_1.check_block_region_2()

def test_check_url_region_2(): 
  script_1.check_url_region_2()

def test_check_title_region_2():
  script_1.check_title_region_2()
  
def test_report():
  script_1.report()