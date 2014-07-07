#coding=utf-8
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

def index(request):
	return HttpResponsePermanentRedirect(reverse('posts'))