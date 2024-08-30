from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Todo, Comment
from .forms import TodoForm, TodoUpdateForm, CommentForm


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


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = "todo_create.html"

    form_class = TodoForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("todo_detail", kwargs={"pk": self.object.id})


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = "todo_update.html"

    form_class = TodoUpdateForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user and not self.request.user.is_superuser:
            raise Http404("해당 To Do를 수정할 권한이 없습니다.")
        return obj

    def get_success_url(self):
        return reverse_lazy("todo_detail", kwargs={"pk": self.object.id})


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    queryset = Todo.objects.all().prefetch_related("comments", "comments__user")
    template_name = "todo_info.html"
    pk_url_kwarg = "pk"  # URL에서 사용할 매개변수를 명시적으로 설정

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        # 'user' 대신 실제 모델에 있는 필드명을 사용해야 합니다. 예: 'author'
        if obj.user != self.request.user and not self.request.user.is_superuser:
            raise Http404("You do not have permission to view this Todo.")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = self.object.comments.order_by("-created_at")
        paginator = Paginator(comments, 5)
        context["comment_form"] = CommentForm()
        context["page_obj"] = paginator.get_page(self.request.GET.get("page"))
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["message"]
    pk_url_kwarg = "pk"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.todo = Todo.objects.get(id=self.kwargs["pk"])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("todo_detail", kwargs={"pk": self.kwargs["pk"]})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ["message"]

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user and not self.request.user.is_superuser:
            raise Http404("해당 댓글을 수정할 권한이 없습니다.")
        return obj

    def get_success_url(self):
        return reverse_lazy("todo_detail", kwargs={"pk": self.object.todo.id})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user and not self.request.user.is_superuser:
            raise Http404("해당 댓글을 삭제할 권한이 없습니다.")
        return obj

    def get_success_url(self):
        return reverse_lazy("todo_detail", kwargs={"pk": self.object.todo.id})
