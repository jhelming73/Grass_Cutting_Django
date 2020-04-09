from django.urls import path
from . import views

urlpatterns = [
    path('', views.lawnmower_list, name='lawnmower_list'),
    path('lawnmowers/<int:pk>', views.lawnmower_detail, name='lawnmower_detail'),
    path('lawnmowers/new', views.lawnmower_create, name='lawnmower_create'),
    path('lawnmowers/<int:pk>/delete', views.lawnmower_delete, name='lawnmower_delete'),
    path('lawnmowers/<int:pk>/edit', views.lawnmower_edit, name='lawnmower_edit'),
        
    path('fertilizers/', views.fertilizer_list, name='fertilizer_list'),
    path('fertilizers/<int:pk>', views.fertilizer_detail, name='fertilizer_detail'),
    path('fertilizers/new', views.fertilizer_create, name='fertilizer_create'),
    path('fertilizers/<int:pk>/delete', views.fertilizer_delete, name='fertilizer_delete'),
    path('fertilizers/<int:pk>/edit', views.fertilizer_edit, name='fertilizer_edit')
]