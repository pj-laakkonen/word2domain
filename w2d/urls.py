from django.urls import path
from . import views

urlpatterns = [
    path('en/<int:pk>/', views.WordDetailEN.as_view()),
    path('en/', views.WordListEN.as_view()),
    path('domains/', views.get_domains),
]
