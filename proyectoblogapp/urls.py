from django.urls import path

from proyectoblogapp import views

urlpatterns = [
    path('',views.home, name="Home"),
]
