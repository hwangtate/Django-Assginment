from django.shortcuts import render
from .fake_db import user_db


def user_list(request):
    context = {"users": user_db}
    return render(request, "user_list.html", context)


def user_info(request, user_id):
    context = {"user": user_db[user_id]}
    return render(request, "user_info.html", context)
