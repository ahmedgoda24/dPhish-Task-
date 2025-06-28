
from django.contrib import admin
from django.urls import path

from ipinfo import views

urlpatterns = [
   path('ip/', views.IPSubmitView.as_view(), name='ip_submit'),
   path('ip-process/', views.IPSubmitprocessView.as_view(), name='ip_process'),
   path('data/', views.IPAddressListView.as_view(), name='ip-list'),

    
]
