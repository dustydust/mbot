from django.contrib import admin
from apps.robot.models import Robot


class RobotAdmin(admin.ModelAdmin):
    pass

admin.site.register(Robot, RobotAdmin)