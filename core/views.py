# Create your views here.
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "home.html",
    )
