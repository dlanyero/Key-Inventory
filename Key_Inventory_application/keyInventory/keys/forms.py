from django import forms
from .models import building, keytype, key, keystatus, keyissue
from django.forms import ModelMultipleChoiceField


class buildingForm(forms.ModelForm):

    class Meta:
        model = building
        fields = ['name', 'code', 'is_residential', 'is_inactive', 'version']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(buildingForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(buildingForm, self).is_valid()

    def full_clean(self):
        return super(buildingForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_code(self):
        code = self.cleaned_data.get("code", None)
        return code

    def clean_is_residential(self):
        is_residential = self.cleaned_data.get("is_residential", None)
        return is_residential

    def clean_is_inactive(self):
        is_inactive = self.cleaned_data.get("is_inactive", None)
        return is_inactive

    def clean_version(self):
        version = self.cleaned_data.get("version", None)
        return version

    def clean(self):
        return super(buildingForm, self).clean()

    def validate_unique(self):
        return super(buildingForm, self).validate_unique()

    def save(self, commit=True):
        return super(buildingForm, self).save(commit)


class keytypeForm(forms.ModelForm):

    class Meta:
        model = keytype
        fields = ['code', 'manu_info', 'description', 'building_id']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


    def __init__(self, *args, **kwargs):
        super(keytypeForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(keytypeForm, self).is_valid()

    def full_clean(self):
        return super(keytypeForm, self).full_clean()

    def clean_code(self):
        code = self.cleaned_data.get("code", None)
        return code

    def clean_manu_info(self):
        manu_info= self.cleaned_data.get("manu_info", None)
        return manu_info

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_building_id(self):
        building_id = self.cleaned_data.get("building_id", None)
        return building_id

    def clean(self):
        return super(keytypeForm, self).clean()

    def validate_unique(self):
        return super(keytypeForm, self).validate_unique()

    def save(self, commit=True):
        return super(keytypeForm, self).save(commit)




class keyForm(forms.ModelForm):

    class Meta:
        model = key
        fields = ['identifier', 'number', 'keytype_id']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(keyForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(keyForm, self).is_valid()

    def full_clean(self):
        return super(keyForm, self).full_clean()

    def clean_identifier(self):
        identifier = self.cleaned_data.get("identifier", None)
        return identifier

    def clean_number(self):
        number = self.cleaned_data.get("number", None)
        return number

    def clean_keytype_id(self):
        keytype_id = self.cleaned_data.get("keytype_id", None)
        return keytype_id

    def clean(self):
        return super(keyForm, self).clean()

    def validate_unique(self):
        return super(keyForm, self).validate_unique()

    def save(self, commit=True):
        return super(keyForm, self).save(commit)


class keystatusForm(forms.ModelForm):

    class Meta:
        model = keystatus
        fields = ['identifier', 'label', 'order', 'is_active']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(keystatusForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(keystatusForm, self).is_valid()

    def full_clean(self):
        return super(keystatusForm, self).full_clean()

    def clean_identifier(self):
        identifier = self.cleaned_data.get("identifier", None)
        return identifier

    def clean_size(self):
        size = self.cleaned_data.get("size", None)
        return size

    def clean_label(self):
        label = self.cleaned_data.get("label", None)
        return label

    def clean_order(self):
        order = self.cleaned_data.get("order", None)
        return order

    def clean_is_active(self):
        is_active = self.cleaned_data.get("is_active", None)
        return is_active

    def clean(self):
        return super(keystatusForm, self).clean()

    def validate_unique(self):
        return super(keystatusForm, self).validate_unique()

    def save(self, commit=True):
        return super(keystatusForm, self).save(commit)


class keyissueForm(forms.ModelForm):

    class Meta:
        model = keyissue
        fields = ["identifier", "key_id", "keystatus_id", "start_date", "start_date", "ownder_id", "person_id", "note"]
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(keyissueForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(keyissueForm, self).is_valid()

    def full_clean(self):
        return super(keyissueForm, self).full_clean()

    def clean_identifier(self):
        identifier = self.cleaned_data.get("identifier", None)
        return identifier

    def clean_key_id(self):
        key_id = self.cleaned_data.get("key_id", None)
        return key_id

    def clean_keystatus_id(self):
        keystatus_id = self.cleaned_data.get("keystatus_id", None)
        return keystatus_id

    def clean_start_date(self):
        start_date = self.cleaned_data.get("start_date", None)
        return start_date

    def clean_start_date(self):
        start_date = self.cleaned_data.get("start_date", None)
        return start_date

    def clean_ownder_id(self):
        ownder_id = self.cleaned_data.get("ownder_id", None)
        return ownder_id

    def clean_person_id(self):
        person_id = self.cleaned_data.get("person_id", None)
        return person_id

    def clean_note(self):
        note = self.cleaned_data.get("note", None)
        return note

    def clean(self):
        return super(keyissueForm, self).clean()

    def validate_unique(self):
        return super(keyissueForm, self).validate_unique()

    def save(self, commit=True):
        return super(keyissueForm, self).save(commit)



