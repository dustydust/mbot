from django.contrib import admin
from apps.robot.models import Robot
from apps.exchange.models import Exchange
from apps.strategy.models import Strategy


class RobotAdmin(admin.ModelAdmin):
    pass


class ExchangeAdmin(admin.ModelAdmin):
    pass


class StrategyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Robot, RobotAdmin)
admin.site.register(Exchange, ExchangeAdmin)
admin.site.register(Strategy, StrategyAdmin)
