#coding=utf-8

from django.shortcuts import render_to_response
from blog.models import Post

def posts_list(request):
	posts = Post.objects.all()
	return render_to_response('index.html', {'posts':posts})


def post_detail(request, post_id):
	post = Post.objects.get(id=post_id)
	return render_to_response('post_detail.html', {'post':post})


def posts_by_date(request, post_date):
    pass

def posts_by_category(request, category_id):
    pass

def posts_by_tag(request, tag):
    pass

def posts_list(request):
    pass

def post_edit(request, post):
    pass