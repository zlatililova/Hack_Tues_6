from django.urls import path
from . import views
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('', views.index, name = "home" ),
    path("create/", views.create, name = "create-page"),

] 