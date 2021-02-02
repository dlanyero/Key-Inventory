from django.db import models

class building(models.Model):
    identifier = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=6, null=False)
    is_residential = models.BooleanField(null=False)
    is_inactive = models.BooleanField(null=False)
    version = models.IntegerField(null=True)

    def _str_(self):
        return self.identifier

class keytype(models.Model):
    identifier = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, null=False)
    manu_info = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=True)
    building_id = models.ForeignKey(building, on_delete=models.SET_NULL, blank=True, null=True)
    def _str_(self):
        return self.identifier

#class keytypes
class key(models.Model):
    identifier = models.CharField(max_length=255, unique=True)
    number = models.IntegerField(null=False)
    keytype_id = models.ForeignKey(keytype,  on_delete=models.CASCADE, blank= False, null=False)

    def _str_(self):
        return self.identifier



class keystatus(models.Model):
    identifier = models.CharField(max_length = 255, unique = True)
    label = models.CharField(max_length=100, null=False)
    order = models.IntegerField(null=False)
    is_active = models.BooleanField(null=False)

    def _str_(self):
        return self.identifier

class keyissue(models.Model):
    identifier = models.CharField(max_length=255, unique=True)
    key_id = models.ForeignKey(key, on_delete=models.CASCADE, blank=False, null=False)
    keystatus_id = models.ForeignKey(keystatus, on_delete=models.CASCADE, blank=False, null=False)
    start_date = models.DateTimeField(null=True)
    End_date = models.DateTimeField(null=True)
    ownder_id = models.CharField(max_length=6, null=True)
    person_id = models.CharField(max_length=6, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)

    def _str_(self):
        return self.identifier

