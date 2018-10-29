from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),

    #new window with id num
    path('<int:album_id>/', views.detail, name='details'),
]
