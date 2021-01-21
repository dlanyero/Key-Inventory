from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import keytype
from ..forms import keytypeForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404
#imports for the new function based class
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
#from braces import SuperuserRequiredMixin


class keytypeListView(ListView):
    model = keytype
    template_name = "keys/keytype_list.html"
    paginate_by = 20
    context_object_name = "keytype_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        super(keytypeListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keytypeListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keytypeListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(keytypeListView, self).get_queryset()

    def get_allow_empty(self):
        return super(keytypeListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(keytypeListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(keytypeListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(keytypeListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(keytypeListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(keytypeListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(keytypeListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keytypeListView, self).get_template_names()


class keytypeDetailView(DetailView):
    model = keytype
    template_name = "keys/keytype_detail.html"
    context_object_name = "keytype"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        super(keytypeDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keytypeDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keytypeDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(keytypeDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(keytypeDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(keytypeDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(keytypeDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(keytypeDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(keytypeDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keytypeDetailView, self).get_template_names()


class keytypeCreateView(CreateView):
    model = keytype
    form_class = keytypeForm
    template_name = "keys/keytype_create.html"
    success_url = reverse_lazy("keytype_list")

    def __init__(self, **kwargs):
        super(keytypeCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(keytypeCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keytypeCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(keytypeCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(keytypeCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(keytypeCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(keytypeCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(keytypeCreateView, self).get_initial()

    def form_invalid(self, form):
        response = super(keytypeCreateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(keytypeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(keytypeCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(keytypeCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keytypeCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("keys:keytype_detail", args=(self.object.pk,))


class keytypeUpdateView(UpdateView):
    model = keytype
    form_class = keytypeForm
    template_name = "keys/keytype_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "keytype"

    def __init__(self, **kwargs):
        super(keytypeUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keytypeUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keytypeUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(keytypeUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(keytypeUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(keytypeUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(keytypeUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(keytypeUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(keytypeUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(keytypeUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(keytypeUpdateView, self).get_initial()

    def form_invalid(self, form):
        response = super(keytypeUpdateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(keytypeUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(keytypeUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(keytypeUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(keytypeUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keytypeUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("keys:keytype_detail", args=(self.object.pk,))


class keytypeDeleteView(DeleteView):
    model = keytype
    template_name = "keys/keytype_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "keytype"

    def __init__(self, **kwargs):
        super(keytypeDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keytypeDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(keytypeDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(keytypeDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(keytypeDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(keytypeDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(keytypeDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(keytypeDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(keytypeDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(keytypeDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keytypeDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("keys:keytype_list")


@permission_required("admin.can_add_log_entry")
def keytype_deleteAll(request):
    template = "keys/keytype_deleteAll.html"

    prompt = {'warning': 'Once deleted, you will not be able to retrieve any of the records. Ensure that you are absolutely sure about you decition before you delete.'}

    if request.method == "GET":
        return render(request, template, prompt)

    keytype.objects.all().delete()
    response = redirect('/keys/keytypes/')
    return response