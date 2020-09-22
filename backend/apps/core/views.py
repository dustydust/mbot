from django.shortcuts import render
from django.http import HttpResponse
from background_task import background
from background_task.models import *
from apps.exchange.models import ExchangeBittrex


from django.db import models

obj_a = {
    'cnt' : 0
}

obj_b = {
    'cnt' : 0
}


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
    r = ExchangeBittrex.get_ticker("btc-ltc")
    print(r.json())


def makereq(request):
    repeat_ticker(schedule=10)
    print("makereq")
    return HttpResponse("R")


def runtask(request):
    # Here we select a strategy to fire
    return HttpResponse("R")


