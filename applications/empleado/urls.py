from django.contrib import admin  
from django.urls import path  
from applications.empleado import views

app_name = 'empleado'

urlpatterns = [  
    path('new', views.emp,name='new'),  
    path('list',views.show,name='list'),  
    path('edit/<int:id>', views.edit,name='edit'),  
    path('update/<int:id>', views.update,name='update'),  
    path('delete/<int:id>', views.destroy,name='delete'),  
]  