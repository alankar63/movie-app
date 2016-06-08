from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^([0-9a-zA-Z ~@#$^*()_+=[\]{}|\\,.?:-]+)/$', views.index, name="index"),
    url(r'^$', views.hello, name='test'),
]
