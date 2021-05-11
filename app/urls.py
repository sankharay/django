from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus),
    path('add', views.add),
    path('travel',views.travel)
]