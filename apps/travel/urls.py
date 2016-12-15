from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='travel'),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^add$', views.add, name='add'),
	url(r'^addtravel$', views.addtravel, name='addtravel'),
	url(r'^destination/(?P<id>\d+)$', views.destination, name='destination'),
	url(r'^join/(?P<id>\d+)$', views.join, name='join')
]
