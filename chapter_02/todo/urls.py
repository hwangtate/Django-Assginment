from django.urls import path
from . import views

urlpatterns = [
    path("", views.TodoListView.as_view(), name="todo_list"),
    path("<int:todo_id>/", views.TodoDetailView.as_view(), name="todo_detail"),
    path("create/", views.TodoCreateView.as_view(), name="todo_create"),
    path("<int:pk>/update/", views.TodoUpdateView.as_view(), name="todo_update"),
    path("<int:pk>/delete/", views.TodoDeleteView.as_view(), name="todo_delete"),
]
