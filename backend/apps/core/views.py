from django.http import HttpResponse
from background_task import background
from background_task.models import *
from apps.exchange.models import Bittrex
from apps.strategy.models import Strategy

from apps.common.requests import Request
import json
from apps.exchange.models import PairHistory
from datetime import date
from datetime import timedelta

obj_a = {
    'cnt' : 0
}

obj_b = {
    'cnt' : 0
}

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


@background(schedule=1)
def _task_a(obj):
    obj['cnt'] = obj['cnt'] + 1
    # test
    print('A Check!', obj['cnt'])


@background(schedule=1)
def _task_b(obj):
    obj['cnt'] = obj['cnt'] + 1
    print('B Check!', obj['cnt'])


def index(request):
    # all_entries = Entry.objects.all()
    b = Task.objects.all()
    print(b)
    return HttpResponse("Hi")


def createtask(request):
    _task_a(obj_a, repeat=5)
    _task_b(obj_b, repeat=2)
    return HttpResponse("Created")


def deletetasks(request):
    b = Task.objects.all().delete()
    # b.objects.all().delete()
    return HttpResponse("Deleted")


@background(schedule=1)
def repeat_ticker():
    ticker = Bittrex.get_ticker("ltc-btc")
    print(ticker)


def makereq(request):
    repeat_ticker(schedule=2, repeat=5)
    print("makereq")
    return HttpResponse("R")

# TODO:
# 1. Fill from last record
# 2. Fill with range

def fillhistory(request):
    candle_interval = "MINUTE_1"
    market_symbol = "USDT-BTC"

    start_date = date(2016, 10, 12)
    end_date = date(2021, 4, 29)
    market_sym_exp = market_symbol.split("-")

    for single_date in daterange(start_date, end_date):
        year = single_date.strftime("%Y")
        month = single_date.strftime("%m")
        day = single_date.strftime("%d")

        bittrex_api_link = f"https://api.bittrex.com/v3/markets/{market_sym_exp[1]}-{market_sym_exp[0]}" \
            f"/candles/{candle_interval}/historical/{year}/{month}/{day}"
        response = Request.get(bittrex_api_link)

        if "code" in response.json():
            return print("ERROR: ", response.json()["code"])
        else:
            for entry in response.json():
                new_record = PairHistory(
                    starts_at=entry["startsAt"],
                    pair=market_symbol,
                    open=entry["open"],
                    high=entry["high"],
                    low=entry["low"],
                    close=entry["close"],
                    volume=entry["volume"],
                    quote_volume=entry["quoteVolume"]
                )
                new_record.save()
            print(f"Responce of {single_date} contains {len(response.json())} records")

    return HttpResponse("Started")

#########


@background(schedule=1)
def process_strategy(strategy_id: str = ""):
    strategy_record = Strategy.objects.get(name=strategy_id)
    strategy_map = strategy_record.get_strategy(strategy_record)
    strategy_map.go()


def run_task(request):
    # Here we select a strategy to fire
    # schedule -- start after | repeat -- repeat every
    strategy_id = "first_strat"
    process_strategy(strategy_id, schedule=1, repeat=1)  # Here we can override schedule and repeat
    return HttpResponse("Runtask")


@background(schedule=1)
def process_backtest(strategy_id: str = ""):
    strategy_record = Strategy.objects.get(name=strategy_id)
    strategy_map = strategy_record.get_strategy(strategy_record)
    strategy_map.go()

def run_backtest(request):
    strategy_id = "backtest1"
    process_strategy(strategy_id, schedule=1)  # Here we can override schedule and repeat
    return HttpResponse("Runtask")