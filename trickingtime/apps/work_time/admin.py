from django.contrib import admin

from .models import (
    WorkDay,
    WorkEntry,
)


class WorkDayAdmin(admin.ModelAdmin):
    readonly_fields = ('day', 'slug',)


class WorkEntryAdmin(admin.ModelAdmin):
    readonly_fields = ('duration', 'duration_decimal',)


admin.site.register(WorkDay, WorkDayAdmin)
admin.site.register(WorkEntry, WorkEntryAdmin)
