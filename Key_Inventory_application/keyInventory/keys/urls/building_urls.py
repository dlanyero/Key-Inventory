from django.conf.urls import url
from ..views import (buildingListView, buildingCreateView, buildingDetailView,
                     buildingUpdateView, buildingDeleteView, building_deleteAll )
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        buildingCreateView.as_view(),
        name="building_create"),

    url(r'^building_deleteAll/$',  # NOQA
        building_deleteAll,
        name="building_deleteAll"),

    url(r'^(?P<pk>\d+)/update/$',
        buildingUpdateView.as_view(),
        name="building_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        buildingDeleteView.as_view(),
        name="building_delete"),

    url(r'^(?P<pk>\d+)/$',
        buildingDetailView.as_view(),
        name="building_detail"),

    url(r'^$',
        buildingListView.as_view(),
        name="building_list"),
]