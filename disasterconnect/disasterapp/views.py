from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "disasterapp/home.html")


def volunteer_login(request):
    return HttpResponse("Volunteer Login Page (placeholder)")


def supervisor_login(request):
    return HttpResponse("Supervisor Login Page (placeholder)")


def admin_login(request):
    return HttpResponse("Admin Login Page (placeholder)")
