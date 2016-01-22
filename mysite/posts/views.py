from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

# Create your views here.
def posts_create(request):
	context = {
		"title": "Create"
	}
	return render(request, "index.html", context)

def posts_detail(request, id):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": "Detail",
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

#posts_list shows all posts, like front page
def posts_list(request):
	queryset = Post.objects.all()
	q_length = len(Post.objects.all())
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