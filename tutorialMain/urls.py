from django.urls import path

from . import views


app_name = 'tutorialMain'

urlpatterns = [ 
    path('', views.homeIndex, name='homeIndex'),
    path('post:<slug:slug>/<int:pk>/', views.tutorialIndex, name='singleIndex'),
]
