from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from disasterapp import views

urlpatterns = [
     path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    # Volunteer
    path(
        "volunteer/signup/",
        views.signup_view,
        {"user_type": "volunteer"},
        name="volunteer_signup",
    ),
    path(
        "volunteer/login/",
        views.login_view,
        {"user_type": "volunteer"},
        name="volunteer_login",
    ),
    # Supervisor
    path(
        "supervisor/signup/",
        views.signup_view,
        {"user_type": "supervisor"},
        name="supervisor_signup",
    ),
    path(
        "supervisor/login/",
        views.login_view,
        {"user_type": "supervisor"},
        name="supervisor_login",
    ),
    # Admin
    path(
        "adminuser/signup/",
        views.signup_view,
        {"user_type": "adminuser"},
        name="admin_signup",
    ),
    path(
        "adminuser/login/",
        views.login_view,
        {"user_type": "adminuser"},
        name="admin_login",
    ),
    path("profile/", views.profile_view, name="profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
