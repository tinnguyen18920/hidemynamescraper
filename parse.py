import re

from bs4 import BeautifulSoup
import pandas as pd


class Parser(object):
    """docstring for """
    def __init__(self,outer_table_list,path=None):
        self.result = {"address":[],
                        "port":[],
                        "country":[],
                        "city":[],
                        "speed":[],
                        "type":[],
                        "anonymity":[]
                    }
        self.path = path
        self.outer_table_list = outer_table_list
                    
    def do_extract(self):
        for outer_table in self.outer_table_list:
            soup = BeautifulSoup(outer_table,"html.parser")
            rows = soup.find("tbody").find_all("tr",recursive=False)
            if rows:
                pass
            else:
                return False

            for row in rows:
                data = {}
                tds = row.find_all("td",recursive=False)

                address = tds[0].text.strip()
                port = tds[1].text.strip()
                country = tds[2].text.strip()
                try:
                    city = re.search(r'\"(.+)\"',country).group(1)
                    country = country.split("\"%s" %city)[0].strip()
                except AttributeError:
                    city = ""
                speed = tds[3].text.strip()
                type = tds[4].text.strip()
                anonymity = tds[5].text.strip()
                self.result["address"].append(address)
                self.result["port"].append(port)
                self.result["country"].append(country)
                self.result["city"].append(city)
                self.result["speed"].append(speed)
                self.result["type"].append(type)
                self.result["anonymity"].append(anonymity)
    
    def to_csv(self):
        

        df = pd.DataFrame(self.result).to_csv(self.path,index=False)

        return self.path

    def excute(self):
        self.do_extract()
        if self.path:
            print("Saving to %s" % self.path)
            return self.to_csv()   
        else:
            return self.result