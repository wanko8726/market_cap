from django import forms
from django.core import validators


class MarketCapForm(forms.Form):
    # ============================================================
    # フォーム定義　ここから
    # ============================================================
    # coin_id : 一意指定
    is_select_coin_id = forms.BooleanField(
        label="is_select_coin_id",
        required=False,
    )
    coin_id = forms.IntegerField(
        label="coin_id",
        validators=[validators.MinValueValidator(0)],
        required=False,
    )

    # coin_name : 一意指定
    is_select_coin_name = forms.BooleanField(
        label="is_select_coin_name",
        required=False,
    )
    coin_name = forms.CharField(
        label="coin_name",
        max_length=255,
        required=False,
    )

    # coin_name : 一意指定
    is_select_coin_code = forms.BooleanField(
        label="is_select_coin_code",
        required=False,
    )
    coin_code = forms.CharField(
        label="coin_code",
        max_length=20,
        required=False,
    )

    # price : 範囲指定 = 以上、以下 のいずれか、または両方
    is_select_price = forms.BooleanField(
        label="is_select_price",
        required=False,
    )
    min_price = forms.IntegerField(
        label="min_price",
        required=False,
    )
    max_price = forms.IntegerField(
        label="max_price",
        required=False,
    )

    # 1h : 範囲指定 = 以上、以下 のいずれか、または両方
    is_select_1h = forms.BooleanField(
        label="is_select_1h",
        required=False,
    )
    min_1h = forms.IntegerField(
        label="min_1h",
        required=False,
    )
    max_1h = forms.IntegerField(
        label="max_1h",
        required=False,
    )

    # 24h : 範囲指定 = 以上、以下 のいずれか、または両方
    is_select_24h = forms.BooleanField(
        label="is_select_24h",
        required=False,
    )
    min_24h = forms.IntegerField(
        label="min_24h",
        required=False,
    )
    max_24h = forms.IntegerField(
        label="max_24h",
        required=False,
    )

    # 7d : 範囲指定 = 以上、以下 のいずれか、または両方
    is_select_7d = forms.BooleanField(
        label="is_select_7d",
        required=False,
    )
    min_7d = forms.IntegerField(
        label="min_7d",
        required=False,
    )
    max_7d = forms.IntegerField(
        label="max_7d",
        required=False,
    )

    # 24h_volume : 範囲指定 = 以上、以下 のいずれか、または両方
    is_select_24h_volume = forms.BooleanField(
        label="is_select_24h_volume",
        required=False,
    )
    min_24h_volume = forms.IntegerField(
        label="min_24h_volume",
        required=False,
    )
    max_24h_volume = forms.IntegerField(
        label="max_24h_volume",
        required=False,
    )

    # market_cap : 範囲指定 = 以上、以下 のいずれか、または両方
    is_select_market_cap = forms.BooleanField(
        label="is_select_market_cap",
        required=False,
    )
    min_market_cap = forms.IntegerField(
        label="min_market_cap",
        required=False,
    )
    max_market_cap = forms.IntegerField(
        label="max_market_cap",
        required=False,
    )

    # ============================================================
    # フォーム定義　ここまで
    # ============================================================

    def __str__(self):
        return str(["{}={}".format(key, value) for key, value in self.__dict__.items()])
