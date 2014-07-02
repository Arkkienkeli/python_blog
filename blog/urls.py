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
    url(r'^admin/', include(admin.site.urls)),
)