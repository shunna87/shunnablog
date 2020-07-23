from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog),
    path('article/<int:article_id>/', views.detail),
]
