from django.urls import path

from work_time.api import views as work_time_views

v1_urlpatterns = [
    path(
        route='work-entries/',
        view=work_time_views.WorkEntryListCreateAPIView.as_view(),
        name='work-entries'
    ),
    path(
        route='work-entries/<uuid:uuid>/',
        view=work_time_views.WorkEntryRUDAPIView.as_view(),
        name='work-entries'
    ),
]
