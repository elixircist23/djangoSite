from django.conf.urls import url, include
from django.contrib import admin

from .views import (
	posts_list,
	posts_create,
	posts_detail,
	posts_update,
	posts_delete,
	)

urlpatterns = [
	url(r'^$', "posts.views.posts_list"),
    url(r'^create/$', "posts.views.posts_create"),
    url(r'^detail/(?P<id>\d)$', "posts.views.posts_detail"),
    url(r'^update/$', "posts.views.posts_update"),
    url(r'^delete/$', "posts.views.posts_delete"),
	]
