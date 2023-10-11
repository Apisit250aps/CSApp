from django.contrib import admin

from . import models
# Register your models here.


@admin.register(models.SchoolYear)
class SchoolYearAdmin(admin.ModelAdmin):
    list_display = [
        'year'
    ]

@admin.register(models.TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = [
        'year',
        'term',
        'class_year',
        'date',
        'subject_name',
        'class_room'
    ]