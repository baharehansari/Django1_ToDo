from django.urls import path
from . import views


urlpatterns = [
    path('',views.homePage),
    path('hello/', views.helloPage, name='hello'),
    path('showinfo/<int:x>/', views.showinfo, name='showinfo'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'), 
    path('create/', views.create, name='create'),  
]