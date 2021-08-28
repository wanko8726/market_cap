from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from market_cap.models import MarketCap, MarketCapList, MarketCapFormModel
from .forms import MarketCapForm


def view_market_cap(request):
    market_caps = []
    form = MarketCapForm(request.POST or None)
    if form.is_valid():
        market_cap_form_model = MarketCapFormModel()
        market_cap_form_model.is_select_coin_id = form.cleaned_data["is_select_coin_id"]
        market_cap_form_model.is_select_coin_name = form.cleaned_data["is_select_coin_name"]
        market_cap_form_model.is_select_coin_code = form.cleaned_data["is_select_coin_code"]
        market_cap_form_model.is_select_price = form.cleaned_data["is_select_price"]
        market_cap_form_model.is_select_1h = form.cleaned_data["is_select_1h"]
        market_cap_form_model.is_select_24h = form.cleaned_data["is_select_24h"]
        market_cap_form_model.is_select_7d = form.cleaned_data["is_select_7d"]
        market_cap_form_model.is_select_24h_volume = form.cleaned_data["is_select_24h_volume"]
        market_cap_form_model.is_select_market_cap = form.cleaned_data["is_select_market_cap"]

        market_cap_form_model.coin_id = form.cleaned_data["coin_id"]
        market_cap_form_model.coin_name = form.cleaned_data["coin_name"]
        market_cap_form_model.coin_code = form.cleaned_data["coin_code"]
        market_cap_form_model.min_price = form.cleaned_data["min_price"]
        market_cap_form_model.max_price = form.cleaned_data["max_price"]
        market_cap_form_model.min_1h = form.cleaned_data["min_1h"]
        market_cap_form_model.max_1h = form.cleaned_data["max_1h"]
        market_cap_form_model.min_24h = form.cleaned_data["min_24h"]
        market_cap_form_model.max_24h = form.cleaned_data["max_24h"]
        market_cap_form_model.min_7d = form.cleaned_data["min_7d"]
        market_cap_form_model.max_7d = form.cleaned_data["max_7d"]
        market_cap_form_model.min_24h_volume = form.cleaned_data["min_24h_volume"]
        market_cap_form_model.max_24h_volume = form.cleaned_data["max_24h_volume"]
        market_cap_form_model.min_market_cap = form.cleaned_data["min_market_cap"]
        market_cap_form_model.max_market_cap = form.cleaned_data["max_market_cap"]

        condition_coin_id = Q()
        condition_coin_name = Q()
        condition_coin_code = Q()
        condition_min_price = Q()
        condition_max_price = Q()
        condition_min_1h = Q()
        condition_max_1h = Q()
        condition_min_24h = Q()
        condition_max_24h = Q()
        condition_min_7d = Q()
        condition_max_7d = Q()
        condition_min_24h_volume = Q()
        condition_max_24h_volume = Q()
        condition_min_market_cap = Q()
        condition_max_market_cap = Q()

        if market_cap_form_model.is_select_coin_id:
            condition_coin_id = Q(coin_id=market_cap_form_model.coin_id)

        if market_cap_form_model.is_select_coin_name:
            condition_coin_name = Q(coin_name=market_cap_form_model.coin_name)

        if market_cap_form_model.is_select_coin_code:
            condition_coin_code = Q(coin_code=market_cap_form_model.coin_code)

        if market_cap_form_model.is_select_price:
            if market_cap_form_model.min_price is not None:
                condition_min_price = Q(price__gte=market_cap_form_model.min_price)
            if market_cap_form_model.max_price is not None:
                condition_max_price = Q(price__lte=market_cap_form_model.max_price)

        if market_cap_form_model.is_select_1h:
            if market_cap_form_model.min_1h is not None:
                condition_min_1h = Q(h1__gte=market_cap_form_model.min_1h)
            if market_cap_form_model.max_1h is not None:
                condition_max_1h = Q(h1__lte=market_cap_form_model.max_1h)

        if market_cap_form_model.is_select_24h:
            if market_cap_form_model.min_24h is not None:
                condition_min_24h = Q(h24__gte=market_cap_form_model.min_24h)
            if market_cap_form_model.max_24h is not None:
                condition_max_24h = Q(h24__lte=market_cap_form_model.max_24h)

        if market_cap_form_model.is_select_7d:
            if market_cap_form_model.min_7d is not None:
                condition_min_7d = Q(__gte=market_cap_form_model.min_7d)
            if market_cap_form_model.max_7d is not None:
                condition_max_7d = Q(__lte=market_cap_form_model.max_7d)

        if market_cap_form_model.is_select_24h_volume:
            if market_cap_form_model.min_24h_volume is not None:
                condition_min_24h_volume = Q(h24_volume__gte=market_cap_form_model.min_24h_volume)
            if market_cap_form_model.max_24h_volume is not None:
                condition_max_24h_volume = Q(h24_volume__lte=market_cap_form_model.max_24h_volume)

        if market_cap_form_model.is_select_market_cap:
            if market_cap_form_model.min_market_cap is not None:
                condition_min_market_cap = Q(market_cap__gte=market_cap_form_model.min_market_cap)
            if market_cap_form_model.max_market_cap is not None:
                condition_max_market_cap = Q(market_cap__lte=market_cap_form_model.max_market_cap)
        market_caps = MarketCap.objects.filter(
            condition_coin_id &
            condition_coin_name &
            condition_coin_code &
            condition_min_price &
            condition_max_price &
            condition_min_1h &
            condition_max_1h &
            condition_min_24h &
            condition_max_24h &
            condition_min_7d &
            condition_max_7d &
            condition_min_24h_volume &
            condition_max_24h_volume &
            condition_min_market_cap &
            condition_max_market_cap
        )
        # [print(market_cap) for market_cap in market_caps]

    return render(request,
                  "market_cap/view_market_cap.html",
                  {
                      "market_caps": market_caps,
                      "form": form
                   })


def initialize_market_cap_db(request):
    from .service import coinGecko
    from .service.coinGecko import CoinGecko
    market_caps = CoinGecko().get_all_market_caps(1, 92)
    for i in range(0, len(market_caps)):
        MarketCap.objects.create(
            coin_id=market_caps.at[i, "coin_id"],
            coin_name=market_caps.at[i, "coin_name"],
            coin_code=market_caps.at[i, "coin_code"],
            info_url=market_caps.at[i, "info_url"],
            price=market_caps.at[i, "price"],
            h1=market_caps.at[i, "h1"],
            h24=market_caps.at[i, "h24"],
            d7=market_caps.at[i, "d7"],
            h24_volume=market_caps.at[i, "h24_volume"],
            market_cap=market_caps.at[i, "market_cap"],
            sparkline_url=market_caps.at[i, "sparkline_url"]
        )

    return HttpResponse("OK")
