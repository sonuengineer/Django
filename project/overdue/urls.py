from django.urls import path
from .views import validate_task

urlpatterns = [
    path('validate-task/', validate_task),
]
