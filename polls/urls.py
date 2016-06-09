from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^([0-9a-zA-Z ~@#$^*()_+=[\]{}|\\,.?:-]+)/$',
        views.info, name="info"),
    url(r'^$', views.wrong_link, name='wronglink'),
]
