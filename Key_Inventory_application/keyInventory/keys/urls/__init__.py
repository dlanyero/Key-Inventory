from django.conf.urls import include, url
app_name="keys"

urlpatterns = [
    url(r'^building/', include('keys.urls.building_urls')),
    url(r'^keytypes/', include('keys.urls.keytype_urls')),
    url(r'^keys/', include('keys.urls.key_urls')),
    url(r'^keystatus/', include('keys.urls.keystatus_urls')),
    url(r'^keyissue/', include('keys.urls.keyissue_urls')),
    url(r'^upload/', include('keys.urls.data_upload_urls')),
    url(r'^reports/', include('keys.urls.reports_urls')),
    url('', include('keys.urls.building_urls')), # default keys page
]
