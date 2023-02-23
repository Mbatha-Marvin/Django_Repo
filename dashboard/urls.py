from django.urls import path

from .views import home_page_view, dash_view

urlpatterns = [
    
    path('', dash_view, name='dash_home'),
]