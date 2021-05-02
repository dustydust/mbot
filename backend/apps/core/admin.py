from django.contrib import admin
from apps.robot.models import Robot
from apps.exchange.models import Exchange
from apps.exchange.models import Order
from apps.exchange.models import PairHistory
from apps.strategy.models import Strategy



class RobotAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Robot._meta.get_fields()]


class ExchangeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Exchange._meta.get_fields()]


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.get_fields()]

class PairHistoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PairHistory._meta.get_fields()]


class StrategyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Robot, RobotAdmin)
admin.site.register(Exchange, ExchangeAdmin)
admin.site.register(PairHistory, PairHistoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Strategy, StrategyAdmin)
