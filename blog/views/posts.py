#coding=utf-8
from django.http.response import Http404
from datetime import date

from django.db.models import Q
from django.shortcuts import render_to_response
from blog.models import Post

def posts_list(request):
	posts = Post.objects.all()
	return render_to_response('index.html', {'posts':posts})


def post_detail(request, post_id):
	post = Post.objects.get(id=post_id)
	return render_to_response('post_detail.html', {'post':post})


def posts_by_date(request, year, month=None, day=None):

    #import pdb; pdb.set_trace()

    year = int (year)
    if month:
        month = int(month)
    if day:
        day = int(day)
    
    if year<1900:
        raise Http404
    if month and (month<1 or month>12):
        raise Http404
    if day and (day<1 or day>31):
        raise Http404

    q = [Q(date__year=year)]
    if month:
        q.append(Q(date__month = month))
    if day:
        q.append(Q(date__day = day))

    query = q.pop()
    for item in q:
        query |= item
    dat = date(year,month or 1,day or 1)
    posts = Post.objects.filter(query)
    print dat
    context = {'dat':dat,'posts':posts}
    print year, month, day
    return render_to_response('posts_by_date.html', context)


def posts_by_category(request, category_id):
    pass


def posts_by_tag(request, tag):
    pass


def post_edit(request, post):
    pass