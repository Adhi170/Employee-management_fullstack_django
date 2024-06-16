from django.urls import path
from employee_app import  views


urlpatterns = [
    path('', views.index,name="home" ),
    path('create/', views.create_view, ),
    path('display/', views.retrieve_view, ),
    path('delete/<int:did>', views.delete_view, ),
    path('update/<int:uid>', views.update_view, ),
]