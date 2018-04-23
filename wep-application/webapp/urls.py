from django.conf.urls import url

from webapp import views
from webapp.views import IndexView, ServiceView, AboutUsView, ContactView, AdviceView, \
    AdviceDetailView, OrderOfMaster, SubscriberFormView

app_name = 'webapp'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^feedback/$', views.FeedbackFormView.as_view(), name='feedback'),
    url(r'^order_of_master/$', OrderOfMaster.as_view(), name='order_of_master'),
    url(r'^subscribe/$', SubscriberFormView.as_view(), name='subscribe'),
    url(r'^services/$', ServiceView.as_view(), name="services"),
    url(r'^services/(?P<service_slug>[\w-]+)/$', views.ServiceDetailView.as_view(), name="service"),
    url(r'^advices/$', AdviceView.as_view(), name="advices"),
    url(r'^order_of_service/$', views.OrderOfService.as_view(), name="order_of_service"),
    url(r'^advices/(?P<slug>[\w-]+)/$', AdviceDetailView.as_view(), name="advice"),
    url(r'^about_us/$', AboutUsView.as_view(), name='about_us'),
    url(r'^contacts/$', ContactView.as_view(), name='contacts'),
]
