from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.index, name="index"),
    path('main/', views.main, name="main"),
    path('showinfo/<pk>', views.showinfo, name="show"),
    path('detail/<nameurl>', views.detail, name="detail"),
    path('delete/<deleteurl>', views.delete, name="delete"),
]
