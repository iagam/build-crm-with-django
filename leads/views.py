from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    context = {
        "name": "Jay",
        "age": 65,
    }
    return render(request, "second_page.html", context)
