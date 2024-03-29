from django.urls import path ,include
from apps.eventsmodule import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('events',views.eventscategories),
    path('event/<int:EventId>',views.eventscategory),
    path ('filtterevents',views.filtterevents, name="filtterEvents")
    

]