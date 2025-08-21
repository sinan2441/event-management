from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_event, name='create'),
    path('show', views.list_events, name='list'),
    path('edit/<pk>', views.edit_event, name='edit'),
    path('delete/<pk>', views.delete_event, name='delete'),
    path('sign_up', views.sign_up, name='register'),
    path('', views.sign_in, name='login'),
    path('logout', views.sign_out, name='logout'),
]
