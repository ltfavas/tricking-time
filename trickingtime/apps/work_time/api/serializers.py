from rest_framework import serializers

from ..models import (
    WorkDay,
    WorkEntry
)


class WorkDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDay
        fields = ['slug', 'day']


class WorkEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkEntry
        fields = ['day', 'project', 'begin_time', 'end_time',
                  'duration', 'duration_decimal', 'description', ]
