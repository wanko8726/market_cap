from django.db import models

# Create your models here.

from django.db import models


class MarketCapList(list):
    def __init__(self):
        super().__init__()

    @staticmethod
    def read_csv(path):
        import os
        import pandas as pd

        if not os.path.exists(path):
            return

        df = pd.read_csv(path)
        market_cap_list = MarketCapList()
        for i in range(0, len(df)):
            market_cap = MarketCap()
            market_cap.coin_id = int(df.at[i, "coin_id"])
            market_cap.coin_name = str(df.at[i, "coin_name"])
            market_cap.coin_code = str(df.at[i, "coin_code"])
            market_cap.info_url = str(df.at[i, "info_url"])
            market_cap.price = float(df.at[i, "price"])
            market_cap.h1 = float(df.at[i, "h1"])
            market_cap.h24 = float(df.at[i, "h24"])
            market_cap.d7 = float(df.at[i, "d7"])
            market_cap.h24_volume = float(df.at[i, "h24_volume"])
            market_cap.market_cap = float(df.at[i, "market_cap"])
            market_cap.sparkline_url = str(df.at[i, "sparkline_url"])
            market_cap.market_per_trade = float(df.at[i, "market_per_trade"])
            market_cap_list.append(market_cap)

        return market_cap_list


class MarketCap(models.Model):
    coin_id: int = models.IntegerField("coin id", primary_key=True)
    coin_name: str = models.CharField("coin name", max_length=255, null=True, blank=True)
    coin_code: str = models.CharField("coin code", max_length=20, null=True, blank=True)
    info_url: str = models.CharField("info url", max_length=2083, null=True, blank=True)
    price: float = models.FloatField("price", null=True, blank=True)
    h1: float = models.FloatField("h1", null=True, blank=True)
    h24: float = models.FloatField("h24", null=True, blank=True)
    d7: float = models.FloatField("d7", null=True, blank=True)
    h24_volume: float = models.FloatField("h24", null=True, blank=True)
    market_cap: float = models.FloatField("market", null=True, blank=True)
    sparkline_url: str = models.CharField("sparkline url", max_length=2083, null=True, blank=True)
    sparkline_source: str = models.CharField("sparkline source", max_length=20480, null=True, blank=True)

    def __str__(self):
        return str(["{}={}".format(key, value) for key, value in self.__dict__.items()])


class MarketCapFormModel(models.Model):
    # ============================================================
    # 検索条件定義　ここから
    # ============================================================
    # coin_id : 一意指定
    is_select_coin_id = models.BooleanField()
    coin_id = models.IntegerField()

    # coin_name : 一意指定
    is_select_coin_name = models.BooleanField()
    coin_name = models.CharField(max_length=255)

    # coin_name : 一意指定
    is_select_coin_code = models.BooleanField()
    coin_code = models.CharField(max_length=20)

    # price : 範囲指定 = 以上、以下 のいずれか、または両方
    is_select_price = models.BooleanField()
    min_price = models.IntegerField()
    max_price = models.IntegerField()

    # 1h : 範囲指定 = 以上、以下 のいずれか、または両方
    is_select_1h = models.BooleanField()
    min_1h = models.IntegerField()
    max_1h = models.IntegerField()

    # 24h : 範囲指定 = 以上、以下 のいずれか、または両方
    is_select_24h = models.BooleanField()
    min_24h = models.IntegerField()
    max_24h = models.IntegerField()

    # 7d : 範囲指定 = 以上、以下 のいずれか、または両方
    is_select_7d = models.BooleanField()
    min_7d = models.IntegerField()
    max_7d = models.IntegerField()

    # 24h_volume : 範囲指定 = 以上、以下 のいずれか、または両方
    is_select_24h_volume = models.BooleanField()
    min_24h_volume = models.IntegerField()
    max_24h_volume = models.IntegerField()

    # market_cap : 範囲指定 = 以上、以下 のいずれか、または両方
    is_select_market_cap = models.BooleanField()
    min_market_cap = models.IntegerField()
    max_market_cap = models.IntegerField()

    # ============================================================
    # 検索条件定義　ここまで
    # ============================================================

    def __str__(self):
        return str(["{}={}".format(key, value) for key, value in self.__dict__.items()])
