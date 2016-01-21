from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.
def posts_create(request):
	context = {
		"title": "Create"
	}
	return render(request, "index.html", context)

def posts_detail(request):
	context = {
		"title": "Detail"
	}
	return render(request, "index.html", context)

def posts_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset ,
		"title": "List"
	}
	return render(request, "index.html", context)

def posts_update(request):
	context = {
		"title": "Update"
	}
	return render(request, "index.html", context)

def posts_delete(request):
	context = {
		"title": "Delete"
	}
	return render(request, "index.html", context)