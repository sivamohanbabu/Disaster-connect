# disasterconnect/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    # Landing page - accessible to all
    return render(request, 'index.html')

@login_required
def dashboard(request):
    # Dashboard - requires login
    return render(request, 'dashboard.html')
