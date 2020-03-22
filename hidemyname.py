
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# from config import Filter

# prox_filter = Filter()
#options = webdriver.ChromeOptions()

#Some filters
#prox_filter.add_country("VN")
#prox_filter.proxy_speed=800

#url = prox_filter.final_url()

class HidemyName(object):
    """docstring for HidemyName"""
    def __init__(self,chrome):
        self.chrome = chrome
        self.outer_table_list = []
        #self.wait = WebDriverWait(self.chrome, 12)

    def get_outer_table(self):
        try:
            table = WebDriverWait(self.chrome,12).until(EC.presence_of_element_located((By.XPATH,"//table[@class='proxy__t']")))
            outer_table = table.get_attribute('outerHTML')
            self.outer_table_list.append(outer_table)
            #print(outer_table)
            #print(chrome.title)
        except TimeoutException:
            #print("No table")
            #print(chrome.title)
            print("COULD NOT LOAD PAGE")
            self.chrome.close()

    def next(self):
        try:
            next_arrow = WebDriverWait(self.chrome,8).until(EC.presence_of_element_located((By.XPATH,"//li[@class='arrow__right']")))
            next_arrow.find_element_by_tag_name("a").click()
            return True
        except TimeoutException:
            print("Reach the end")
            return False
    def main(self):  
        i = 1
        while True:
            if i == 1:
                self.get_outer_table()
                i += 1
            if self.next():
                self.get_outer_table()
            else:
                break
        self.chrome.close()
        return self.outer_table_list
