from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from django.http import HttpResponse
from .models import CustomUser


def home(request):
    return render(request, "disasterapp/home.html")


def signup_view(request, user_type):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = "volunteer"
            # Latitude and Longitude from hidden fields
            user.latitude = request.POST.get("latitude")
            user.longitude = request.POST.get("longitude")
            user.save()

            # Always redirect to volunteer login since all signups are volunteers
            return redirect("volunteer_login")

    else:
        form = SignUpForm()
    return render(
        request, "disasterapp/signup.html", {"form": form, "user_type": user_type}
    )


def login_view(request, user_type):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user and user.user_type == user_type:
                login(request, user)
                return redirect("profile")  # 👈 redirect instead of HttpResponse
    else:
        form = LoginForm()
    return render(
        request, "disasterapp/login.html", {"form": form, "user_type": user_type}
    )


from django.contrib.auth.decorators import login_required


@login_required
def profile_view(request):
    user = request.user  # current logged-in user
    return render(request, "disasterapp/profile.html", {"user": user})
