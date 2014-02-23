#urls.py
from django.conf.urls import patterns, url
from myblog import views

urlpatterns = patterns('myblog.views',
    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    #url(r'^$', 'stub_view', name="blog_index"),
    #url(r'^posts/(\d+)/$', 'stub_view', name="blog_detail"),
    #r'^posts/(?P<post_id>\d+)/$'
    url(r'^$', 'list_view', name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$', 'detail_view', name="blog_detail"),
)
