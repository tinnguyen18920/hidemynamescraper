import sys

from selenium import webdriver

from hidemyname import HidemyName
from parse import Parser

def main():

    
    url = str(sys.argv[-2])
    path = sys.argv[-1]

    chrome = webdriver.Chrome()
    chrome.get(url)
    hide = HidemyName(chrome)

    data = hide.main()
    extract = Parser(data,path)

    result = extract.excute()
    #print(result)
    print("Done".center(20,"-"))
    
if __name__ == "__main__":
    main()

