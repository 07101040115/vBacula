'''
Created on 

@author: wtsyy
'''
from django.conf.urls import url

from webacula import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^main$',  views.main),
    url(r'^task$',  views.job_list),
    url(r'^restoreJob',  views.job_restore),
    url(r'^backupJob',  views.job_backup),
    url(r'^dummpjson',  views.dummpjson)
]