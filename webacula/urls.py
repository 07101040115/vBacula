'''
Created on 

@author: wtsyy
'''
from django.conf.urls import url

from webacula import views

urlpatterns = [
    url(r'^$',  views.login),
]
