import sys

import pandas as pd
from selenium import webdriver

from checker import ProxyWebChecker
from hidemyname import HidemyName
from parse import Parser

def main():

    
    url = str(sys.argv[-3])
    url_for_proxy_check = str(sys.argv[-2])
    path = sys.argv[-1]


    chrome = webdriver.Chrome()
    chrome.get(url)
    hide = HidemyName(chrome)

    data = hide.main()
    extract = Parser(data,path)

    result = extract.excute()
    
    """
    >>> result = {
            "address": ["1.1.1.1","2.2.2.2"],
            "port": ["3128","8080"],
            "country": [],...
            }
    >>> proxy_list = [n+":"+p for n,p in zip(result['address'],result['port'])]
    >>> proxy_list 
    ["1.1.1.1:3128","2.2.2.2:8080"]
    """
    proxy_list = [n+":"+p for n,p in zip(result['address'],result['port'])]


    print("CHECING PROXIES FOR %s ".center(80,"#") % url_for_proxy_check)
    final = check(url_for_proxy_check,proxy_list)
    df = pd.DataFrame(final).to_csv(path,index=False)
    print("Done".center(80,"-"))


def check(url_for_proxy_check,proxy_list):
        final_proxies = {
                        "Proxies":[],
                        "Time": []
        }            
        checker = ProxyWebChecker(url_for_proxy_check)
        for proxy in proxy_list:
            res = checker(proxy)
            if res:
                final_proxies['Proxies'].append(res[0])
                final_proxies['Time'].append(res[-1])
        return final_proxies

if __name__ == "__main__":
    main()

