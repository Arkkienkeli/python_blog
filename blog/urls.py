from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^posts/$', 'blog.views.posts_list', name='posts'),
    url(r'^posts/([\w\-]+)-(?P<post_id>\d+)/$', 'blog.views.post_detail', name='post_detail'),
    url(r'^posts/(\d+)/(\d+)/(\d+)/$', 'blog.views.posts_by_date', name='posts_by_date'),
    url(r'^posts/category/(\w+)-(\d+)/$', 'blog.views.posts_by_category', name='posts_by_category'),
    url(r'^posts/tag/(\w+)/$', 'blog.views.posts_by_tag', name='posts_by_tag'),
    url(r'^posts/page-(\d+)/$', 'blog.views.posts_list', name='posts_list'),
    url(r'^posts/(\w+)-(\d+)/edit/$', 'blog.views.post_edit', name='post_edit'),

    url(r'^user/(?P<user_id>\d+)/$', 'blog.views.user_profile', name='profile'),
    url(r'^user/(?P<user_id>\d+)/edit$', 'blog.views.user_profile_edit', name='user_profile_edit'),

    url(r'^admin/', include(admin.site.urls)),
)