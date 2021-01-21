from django.conf.urls import url
from ..views import (keytypeListView, keytypeCreateView, keytypeDetailView,
                     keytypeUpdateView, keytypeDeleteView, keytype_deleteAll)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        keytypeCreateView.as_view(),
        name="keytype_create"),

    url(r'^keytype_deleteAll/$',  # NOQA
            keytype_deleteAll,
            name="keytype_deleteAll"),

    url(r'^(?P<pk>\d+)/update/$',
        keytypeUpdateView.as_view(),
        name="keytype_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        keytypeDeleteView.as_view(),
        name="keytype_delete"),

    url(r'^(?P<pk>\d+)/$',
        keytypeDetailView.as_view(),
        name="keytype_detail"),

    url(r'^$',
        keytypeListView.as_view(),
        name="keytype_list"),
]