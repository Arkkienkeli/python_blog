#coding=utf-8
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


def user_profile(request, user_id):
	user = User.objects.get(id=user_id)
	return render_to_response('user_profile.html', {'user':user})


def user_profile_edit(request, user_id):
    pass