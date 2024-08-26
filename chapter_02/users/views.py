from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login


def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login")

    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "registration/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST or None)
        if form.is_valid():
            django_login(request, form.get_user())
            return redirect("/todo")
    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, "registration/login.html", context)
