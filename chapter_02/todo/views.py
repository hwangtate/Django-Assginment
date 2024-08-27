from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Todo
from .forms import TodoForm


def todo_list(request):
    todos = Todo.objects.all().order_by("-created_at")

    q = request.GET.get("q")
    if q:
        todos = todos.filter(title__icontains=q)

    paginator = Paginator(todos, 5)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)

    return render(request, "todo_list.html", {"todos": todos, "page_obj": page_obj})


def todo_detail(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)

    return render(request, "todo_info.html", {"todo": todo})


@login_required(login_url="login")
def todo_create(request):

    form = TodoForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.author = request.user
        todo.save()
        return redirect(reverse("todo_detail", kwargs={"todo_id": todo.id}))

    context = {"form": form}

    return render(request, "todo_create.html", context)


@login_required(login_url="login")
def todo_update(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)

    if request.user != todo.author:
        raise PermissionDenied("You are not authorized to edit this todo.")

    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        todo = form.save()
        return redirect(reverse("todo_detail", kwargs={"todo_id": todo.id}))

    context = {"form": form, "todo": todo}
    return render(request, "todo_update.html", context)


@login_required(login_url="login")
@require_http_methods(["POST"])
def todo_delete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect(reverse("todo_list"))
