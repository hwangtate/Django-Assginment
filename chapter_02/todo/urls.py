from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.TodoListView.as_view(), name="todo_list"),
    path("<int:pk>/", views.TodoDetailView.as_view(), name="todo_detail"),
    path("create/", views.TodoCreateView.as_view(), name="todo_create"),
    path("<int:pk>/update/", views.TodoUpdateView.as_view(), name="todo_update"),
    path("<int:pk>/delete/", views.DeleteView.as_view(), name="todo_delete"),
    path(
        "comment/<int:pk>/create/",
        views.CommentCreateView.as_view(),
        name="comment_create",
    ),
    path(
        "comment/<int:pk>/delete/",
        views.CommentDeleteView.as_view(),
        name="comment_delete",
    ),
    path(
        "comment/<int:pk>/update/",
        views.CommentUpdateView.as_view(),
        name="comment_update",
    ),
    path("summernote/", include("django_summernote.urls")),
]
