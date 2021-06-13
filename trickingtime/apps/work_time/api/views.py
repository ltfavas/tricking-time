from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from ..models import (
    WorkDay,
    WorkEntry
)
from .serializers import (
    WorkDaySerializer,
    WorkEntrySerializer
)


class WorkEntryListCreateAPIView(ListCreateAPIView):
    queryset = WorkEntry.objects.all()
    permission_classes = ()
    serializer_class = WorkEntrySerializer
    lookup_field = 'uuid'


class WorkEntryRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = WorkEntry.objects.all()
    permission_classes = ()
    serializer_class = WorkEntrySerializer
    lookup_field = 'uuid'
