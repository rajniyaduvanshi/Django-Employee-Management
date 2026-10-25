from django.shortcuts import render


def home(request):
    return render(request, "App1/home.html")


def about(request):
    return render(request, "App1/about.html")


def contact(request):
    return render(request, "App1/contact.html")