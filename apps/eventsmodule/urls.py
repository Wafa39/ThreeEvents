from django.urls import path ,include
from apps.eventsmodule import views 

urlpatterns = [
    path('',views.index,name='index'),

]
