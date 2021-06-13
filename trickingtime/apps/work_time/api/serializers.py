from rest_framework import serializers

from ..models import (
    WorkDay,
    WorkEntry
)

from projects.models import Project


class WorkDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDay
        fields = ['uuid', 'slug', 'day']


class WorkEntrySerializer(serializers.ModelSerializer):
    day = serializers.SlugRelatedField(
        many=False,
        slug_field='slug',
        queryset=WorkDay.objects.all()
    )  
    project = serializers.SlugRelatedField(
        many=False,
        slug_field='code_name',
        queryset=Project.objects.all()
    )

    class Meta:
        model = WorkEntry
        fields = ['uuid', 'day', 'project', 'begin_time', 'end_time',
                  'duration', 'duration_decimal', 'description', ]
