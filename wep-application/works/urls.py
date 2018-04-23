from django.conf.urls import url

from works.views import IndexView
from . import views

app_name = 'works'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<filter_slug>[\w-]+)/(?P<category_slug>[\w-]+)/$', views.WorksListView.as_view(), name='works'),
    url(r'^(?P<filter_slug>[\w-]+)/(?P<category_slug>[\w-]+)/all/$', views.AllWorksView.as_view(), name='all_works'),
]
