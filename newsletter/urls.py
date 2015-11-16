from django.conf.urls import patterns, url

from newsletter import views

urlpatterns = patterns('',
  
  url(r'^delete/(?P<pk>\d+)$', views.book_delete, name='book_delete'),
)