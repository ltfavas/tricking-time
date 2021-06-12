from django.urls import path

from projects.api.urls import v1_urlpatterns as projects_v1_urlpatterns
from work_time.api.urls import v1_urlpatterns as work_time_v1_urlpatterns


urlpatterns = [] + projects_v1_urlpatterns + work_time_v1_urlpatterns
