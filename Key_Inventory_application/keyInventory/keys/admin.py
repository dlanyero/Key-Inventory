from django.contrib import admin
from .models import building, keytype, key, keystatus, keyissue

# Register your models here.
admin.site.register(building)
admin.site.register(keytype)
admin.site.register(key)
admin.site.register(keystatus)
admin.site.register(keyissue)