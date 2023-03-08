from django.urls import path
from .views import *

urlpatterns = [
    path('bio/create/', BiodataCreateView.as_view(), name="biodata"),
    path('bio/edit/<int:pk>/', BiodataEditView.as_view(), name="biodata_edit"),
    path('projects/add/', ProjectListCreateView.as_view(), name="projects_view"),
    path('projects/edit/<int:pk>/', ProjectEditView.as_view(), name="projects_edit"),
]