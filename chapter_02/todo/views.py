from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Todo
from .forms import TodoForm


class TodoListView(ListView):
    queryset = Todo.objects.all()
    template_name = "todo_list.html"
    paginate_by = 5
    ordering = ("-created_at",)

    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get("q")

        if q:
            queryset = queryset.filter(title__icontains=q)

        return queryset


class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo_info.html"
    pk_url_kwarg = "todo_id"

    def get_object(self):
        obj = super().get_object()

        if self.request.user.is_superuser or self.request.user == obj.author:
            return obj
        else:
            raise Http404("You are not logged in.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_object().__dict__)
        return context


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = "todo_create.html"
    # fields = ["title", "description", "done"]
    form_class = TodoForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("todo_detail", kwargs={"todo_id": self.object.pk})


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = "todo_update.html"
    form_class = TodoForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if not self.request.user.is_superuser and self.request.user != obj.author:
            raise Http404("You are not authorized to edit this Todo.")

        return obj

    def get_success_url(self):
        return reverse_lazy("todo_detail", kwargs={"todo_id": self.object.pk})


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = "todo_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if not self.request.user.is_superuser and self.request.user != obj.author:
            raise Http404("You are not authorized to delete this Todo.")

        return obj

    def get_success_url(self):
        return reverse_lazy("todo_list")
