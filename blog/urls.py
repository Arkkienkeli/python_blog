from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.views.index',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('blog.views.index',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'index', name='index'),
)
urlpatterns += patterns('blog.views.posts',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^posts/$', 'posts_list', name='posts'),
    url(r'^posts/([\w\-]+)-(?P<post_id>\d+)/$', 'post_detail', name='post_detail'),
    url(r'^posts/(\d+)/(\d+)/(\d+)/$', 'posts_by_date', name='posts_by_date'),
    url(r'^posts/(\d+)/(\d+)/$', 'posts_by_date', name='posts_by_date'),
    url(r'^posts/(\d+)/$', 'posts_by_date', name='posts_by_date'),
    url(r'^posts/category/(\w+)-(\d+)/$', 'posts_by_category', name='posts_by_category'),
    url(r'^posts/tag/(\w+)/$', 'posts_by_tag', name='posts_by_tag'),
    url(r'^posts/page-(\d+)/$', 'posts_list', name='posts_list'),
    url(r'^posts/(\w+)-(\d+)/edit/$', 'post_edit', name='post_edit'),

)
urlpatterns += patterns('blog.views.users',

    url(r'^user/(?P<user_id>\d+)/$', 'user_profile', name='profile'),
    url(r'^user/(?P<user_id>\d+)/edit$', 'user_profile_edit', name='user_profile_edit'),

)