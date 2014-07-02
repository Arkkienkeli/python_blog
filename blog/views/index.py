#coding=utf-8
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import loader, Context
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from blog.models import Post

def index(request):
	return HttpResponsePermanentRedirect(reverse('posts'))


def posts_list(request):
	posts = Post.objects.all()
	return render_to_response('index.html', {'posts':posts})

def post_detail(request,post_id):
	print post_id
	post = Post.objects.get(id=post_id)
	return render_to_response('post_detail.html', {'post':post})