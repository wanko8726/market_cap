import re
import pandas as pd
import os
import sys
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup

from pycoingecko import CoinGeckoAPI

pd.set_option('display.max_columns', 100)


class CoinGecko:
    def __init__(self):
        self.api = CoinGeckoAPI()
        self.coingecko_url = r"https://www.coingecko.com/en"

    def get_coins_list(self):
        coins_list = self.api.get_coins_list()
        print(coins_list)

    def get_coins_markets(self):
        coins_markets = self.api.get_coins_markets()
        print(coins_markets)

    def get_all_market_cap_pages(self, start_page: int = 1, end_page: int = 1):
        print(sys._getframe().f_code.co_name)
        p = Pool(os.cpu_count())
        return p.map(requests.get, [self.coingecko_url + "?page=" + str(i) for i in range(start_page, end_page+1)])

    def get_all_market_caps(self, start_page: int = 1, end_page: int = 1):
        print(sys._getframe().f_code.co_name)
        market_caps_pages = self.get_all_market_cap_pages(start_page, end_page)
        merged_market_caps = []

        p = Pool(os.cpu_count())
        result = p.map(self.get_market_caps, [market_caps_page.content for market_caps_page in market_caps_pages])
        [merged_market_caps.extend(market_caps) for market_caps in result]

        return pd.DataFrame(list(map(lambda marketcap: vars(marketcap), merged_market_caps)))

    def get_market_caps(self, market_caps_page):
        print(sys._getframe().f_code.co_name)
        market_caps = []

        soup = BeautifulSoup(market_caps_page, "html.parser")

        table_rows = soup.find("table").find_all("tr")[1:]

        for row in table_rows:
            market_cap = MarketCap()

            table_data = row.find_all("td")

            market_cap.coin_id = int(table_data[0].find("i")["data-coin-id"])

            coin_name_elements = table_data[2].find_all("a")
            market_cap.coin_name = coin_name_elements[0].text.replace("\n", "")
            market_cap.coin_code = coin_name_elements[1].text.replace("\n", "")
            market_cap.info_url = self.coingecko_url + coin_name_elements[1]["href"].replace("en/", "")

            td_price = table_data[3].find("span")
            td_h1 = table_data[4].find("span")
            td_h24 = table_data[5].find("span")
            td_d7 = table_data[6].find("span")
            h24_volume = table_data[7].find("span")
            mkt_cap = table_data[8].find("span")

            if td_price is not None and td_price.text not in ("?", "N/A"):
                market_cap.price = float(re.sub("[$,]", "", table_data[3].find("span").text))
            if td_h1 is not None and td_h1.text != "?":
                market_cap.h1 = float(table_data[4].find("span").text.replace("%", ""))
            if td_h24 is not None and td_h24.text != "?":
                market_cap.h24 = float(table_data[5].find("span").text.replace("%", ""))
            if td_d7 is not None and td_d7.text != "?":
                market_cap.d7 = float(table_data[6].find("span").text.replace("%", ""))
            if h24_volume is not None and h24_volume.text != "?":
                market_cap.h24_volume = float(re.sub("[$,]", "", table_data[7].find("span").text))
            if mkt_cap is not None and mkt_cap.text != "?":
                market_cap.market_cap = float(re.sub("[$,]", "", table_data[8].find("span").text))

            market_cap.sparkline_url = "https://www.coingecko.com/coins/{}/sparkline".format(market_cap.coin_id)

            market_caps.append(market_cap)

        return market_caps
    #
    # def get_market_caps_selenium(self, page: int = 1):
    #     import chromedriver_binary
    #     from selenium import webdriver
    #
    #     print("current page: " + str(page))
    #
    #     options = webdriver.ChromeOptions()
    #     options.add_argument("--headless")
    #     options.add_argument('--disable-gpu')
    #     options.add_argument('--disable-extensions')
    #     options.add_argument('--proxy-server="direct://"')
    #     options.add_argument('--proxy-bypass-list=*')
    #     options.add_argument('--blink-settings=imagesEnabled=false')
    #     options.add_argument('--lang=ja')
    #     options.add_argument('--no-sandbox')
    #     options.add_argument('--disable-dev-shm-usage')
    #     options.add_argument("--log-level=3")
    #     options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36')
    #     options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #     options.add_experimental_option('useAutomationExtension', False)
    #     options.page_load_strategy = 'eager'
    #
    #     driver = webdriver.Chrome(chrome_options=options)
    #
    #     driver.get(self.coingecko_url + "?page=" + str(page))
    #
    #     dfs = pd.read_html(driver.find_element_by_tag_name("table").get_attribute("outerHTML"))
    #     data_frame = pd.concat(dfs, ignore_index=True)
    #     # print(data_frame[1:2])
    #     # data_frame.to_csv("test.csv")
    #     table_rows = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")[1:]
    #
    #     market_caps = []
    #     for i in range(0, len(table_rows)):
    #         market_cap = MarketCap()
    #         row = table_rows[i]
    #
    #         table_data = row.find_elements_by_tag_name("td")
    #
    #         market_cap.coin_id = int(table_data[0].find_element_by_tag_name("i").get_attribute("data-coin-id"))
    #         coin_name_elements = table_data[2].find_elements_by_tag_name("a")
    #         market_cap.coin_name = str(coin_name_elements[0].get_attribute("textContent")).replace("\n", "")
    #         market_cap.coin_code = str(coin_name_elements[1].get_attribute("textContent")).replace("\n", "")
    #         market_cap.info_url = str(coin_name_elements[1].get_attribute("href"))
    #
    #         price = data_frame.at[i, "Price"]
    #         h1 = data_frame.at[i, "1h"]
    #         h24 = data_frame.at[i, "24h"]
    #         d7 = data_frame.at[i, "7d"]
    #         h24_volume = data_frame.at[i, "24h Volume"]
    #         mkt_cap = data_frame.at[i, "Mkt Cap"]
    #
    #         if not pd.isnull(price):
    #             market_cap.price = float(re.sub("[$,]", "", price))
    #         if not pd.isnull(h1) and h1 != "?":
    #             market_cap.h1 = float(h1.replace("%", ""))
    #         if not pd.isnull(h24) and h24 != "?":
    #             market_cap.h24 = float(h24.replace("%", ""))
    #         if not pd.isnull(d7) and d7 != "?":
    #             market_cap.d7 = float(d7.replace("%", ""))
    #         if not pd.isnull(h24_volume) and h24_volume != "?":
    #             market_cap.h24_volume = float(re.sub("[$,]", "", h24_volume))
    #         if not pd.isnull(mkt_cap) and mkt_cap != "?":
    #             market_cap.market_cap = float(re.sub("[$,]", "", mkt_cap))
    #
    #         market_cap.sparkline_url = "https://www.coingecko.com/coins/{}/sparkline".format(market_cap.coin_id)
    #         market_caps.append(market_cap)
    #         # print(market_cap)
    #
    #     return market_caps

    # def get_market_caps_multi(self, page=1):
    #     p = Pool(os.cpu_count())
    #     result = p.map(self.get_market_caps, range(1, page+1))
    #     merged_result = []
    #     [merged_result.extend(market_caps) for market_caps in result]
    #     return merged_result


class MarketCap:
    coin_id: int = None
    coin_name: str = None
    coin_code: str = None
    info_url: str = None
    price: float = None
    h1: float = None
    h24: float = None
    d7: float = None
    h24_volume: float = None
    market_cap: float = None
    sparkline_url: str = None

    def __init__(self):
        pass

    def __str__(self):
        return str(["{}={}".format(key, value) for key, value in self.__dict__.items()])
