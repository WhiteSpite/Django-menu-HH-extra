from django.urls import path
from .views import *

app_name = 'menu'
urlpatterns = [
    path('', home_view),
    path('<slug:slug>/', MenuDetail.as_view(), name='menu'),
]
