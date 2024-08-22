from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list),
    path("<int:todo_id>/", views.todo_detail),
]
