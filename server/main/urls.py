"""mysite URL Configuration

[...]
"""
from django.conf.urls import url
from django.urls import path


from .views import Index

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
]