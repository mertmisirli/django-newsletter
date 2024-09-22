from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("newsletter", views.newsletter, name="newsletters"),
    path("news-detail/<int:id>", views.news_detail, name="news_detail"),
    path('category-newsletters/<int:category_id>/', views.category_newsletter, name='category_newsletter'),

]