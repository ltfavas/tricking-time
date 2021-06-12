from django.urls import path

from projects.api import views as projects_views

v1_urlpatterns = [
    path(
        route='projects/',
        view=projects_views.ProjectListAPIView.as_view(),
        name='projects'
    ),
]
