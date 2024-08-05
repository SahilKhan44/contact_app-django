from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contact/<int:pk>/edit/', views.contact_edit, name='contact_edit'),
    path('contact/new/', views.contact_new, name='contact_new'),  # New URL for creating contacts
]
