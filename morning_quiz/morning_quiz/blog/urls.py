from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('summit/', views.summit, name='summit'),
    path('save/', views.save, name='save'),
]
