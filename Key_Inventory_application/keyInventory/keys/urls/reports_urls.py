from django.conf.urls import url
from ..views import (keylocation_report, keyuser_report, reports)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^keylocation/$',  # NOQA
        keylocation_report,
        name="keylocation_report"),
    url(r'^keyuser/$',  # NOQA
        keyuser_report,
        name="keyuser_report"),
    url(r'^$',
        reports,
        name="reports"),
]