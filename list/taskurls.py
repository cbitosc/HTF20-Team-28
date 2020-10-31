from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[ path('todo/',views.home,name='todo'),
			  path('/update/<str:pk>',views.update,name='update'),
			  path('/delete/<str:pk>',views.delete,name='delete')
			  # url(regex=r'^todo/$', view=login_user, name='todo'),
			  # url(regex=r'^update/$', view=login_user, name='login'),
			  # url(regex=r'^login/$', view=login_user, name='login'),
			  # url(regex=r'^login/$', view=login_user, name='login'),


]