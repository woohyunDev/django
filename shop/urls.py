from django.urls import path
from . import views

urlpatterns = [  
    path('index/', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
    path('info/<id>', views.showinfo, name = 'info'),
    path('delete/<id>', views.delete, name = 'delete'),
    path('creply/<id>', views.creply, name = 'creply'),
    path('dreply/<pro_id>/<rep_id>', views.dreply, name = 'dreply'),               
]