from django.urls import path 

from . import views

urlpatterns = [
    path('',views.index),
    path('login',views.login),
    path('update/<int:uid>/',views.update),
    path('showdata',views.showdata),
    path('signin',views.signin),
    path('updatedata',views.updatedata),
    path('delete/',views.delete),
    
    
    
]