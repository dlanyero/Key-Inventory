from django.conf.urls import url
from ..views import (keyListView, keyCreateView, keyDetailView,
                     keyUpdateView, keyDeleteView, key_deleteAll)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        keyCreateView.as_view(),
        name="key_create"),

    url(r'^key_deleteAll/$',  # NOQA
        key_deleteAll,
        name="key_deleteAll"),

    url(r'^(?P<pk>\d+)/update/$',
        keyUpdateView.as_view(),
        name="key_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        keyDeleteView.as_view(),
        name="key_delete"),

    url(r'^(?P<pk>\d+)/$',
        keyDetailView.as_view(),
        name="key_detail"),

    url(r'^$',
        keyListView.as_view(),
        name="key_list"),
]