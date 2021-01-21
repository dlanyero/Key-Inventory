from django.conf.urls import url
from ..views import (keyissueListView, keyissueCreateView, keyissueDetailView,
                     keyissueUpdateView, keyissueDeleteView, keyissue_deleteAll)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        keyissueCreateView.as_view(),
        name="keyissue_create"),

    url(r'^keyissue_deleteAll/$',  # NOQA
        keyissue_deleteAll,
        name="keyissue_deleteAll"),

    url(r'^(?P<pk>\d+)/update/$',
        keyissueUpdateView.as_view(),
        name="keyissue_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        keyissueDeleteView.as_view(),
        name="keyissue_delete"),

    url(r'^(?P<pk>\d+)/$',
        keyissueDetailView.as_view(),
        name="keyissue_detail"),

    url(r'^$',
        keyissueListView.as_view(),
        name="keyissue_list"),
]