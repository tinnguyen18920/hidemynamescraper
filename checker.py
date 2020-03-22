



import requests

import pandas as pd
from requests.exceptions import ProxyError, SSLError, ConnectionError, Timeout 


HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"+\
"(KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

class ProxyWebChecker(object):
    """docstring for ProxyWebChecker"""
    def __init__(self, url):
        super(ProxyWebChecker).__init__()
        self._s = requests.session()
        self._s.headers.update(HEADERS)
        self._url = url
        self._time_out = 24

    def __call__(self,proxy,post=False):
        """
        >>> url = "https://stackoverflow.com/"
        >>> proxy_checker = ProxyWebChecker(url)
        >>> proxy = "1.0.0.104:11111111"
        >>> response = proxy_checker(proxy)
        >>> response
        None

        """
        proxies = {"http": proxy, "https": proxy}
        self._s.proxies.update(proxies)
        print("Checking proxy: %s ..." % proxy)
        try:
            if post:
                response = self._s.post(self._url,timeout=self._time_out)
            else:
                response = self._s.get(self._url,timeout=self._time_out)
        except ProxyError as pro_err:
            #return "Proxy Erro %s" % pro_err
            print("Proxy Erro")
            return None
            
        except SSLError as ssl_err:    
            #return "SSL Erro %s" % ssl_err
            print("SSL Erro ")        
            return None
            
        except ConnectionError as con_err:
            print( "Connection Error"    )
            return None
        except Timeout:
            print("Time outed")
            return None
        print((proxy,response.status_code,response.elapsed.total_seconds()))

        #('144.91.116.171:3128', 200, 10.030328)
        return (proxy,response.elapsed.total_seconds())


# def test():
#     url = "https://www.twitch.tv/"
#     pc = ProxyWebChecker(url)
    
#     df = pd.read_csv("proxy_web.csv",usecols=['address','port'])
#     df['port'] = df['port'].apply(str)
#     proxy_list = df[['address','port']].apply(lambda x: ':'.join(x), axis=1)
#     print("CHECING PROXIES FOR %s ".center(80,"#") % url)
#     for proxy in proxy_list[150:170]:

    
#         res = pc(proxy)
#         print(res)
     
    
# if __name__ == "__main__":
#     test()



