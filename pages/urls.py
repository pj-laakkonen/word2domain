from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('w2d/', views.W2DPageView.as_view(), name='w2d'),
    path('about/', views.AboutPageView.as_view(), name='about'),
]

