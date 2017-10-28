from django.conf.urls import url
from health import views

app_name = 'health'

urlpatterns = [
    url(r'^$',views.PatientListView.as_view(),name='plist'),
    url(r'^(?P<pk>\d+)/$',views.PatientDetailView.as_view(),name='pdetail'),
    url(r'^(?P<pk>\d+)/sensor$',views.SensorListView.as_view(),name='slist'),
    url(r'^(?P<id>\d+)/sensor/(?P<pk>\d+)$',views.SensorDetailView.as_view(),name='sdetail'),
]
