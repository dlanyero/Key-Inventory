from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import keystatus
from ..forms import keystatusForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
#from braces import SuperuserRequiredMixin


class keystatusListView(ListView):
    model = keystatus
    template_name = "keys/keystatus_list.html"
    paginate_by = 20
    context_object_name = "keystatus_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        super(keystatusListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keystatusListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keystatusListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(keystatusListView, self).get_queryset()

    def get_allow_empty(self):
        return super(keystatusListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(keystatusListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(keystatusListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(keystatusListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(keystatusListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(keystatusListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(keystatusListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keystatusListView, self).get_template_names()


class keystatusDetailView(DetailView):
    model = keystatus
    template_name = "keys/keystatus_detail.html"
    context_object_name = "keystatus"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        super(keystatusDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keystatusDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keystatusDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(keystatusDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(keystatusDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(keystatusDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(keystatusDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(keystatusDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(keystatusDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keystatusDetailView, self).get_template_names()


class keystatusCreateView(CreateView):
    model = keystatus
    form_class = keystatusForm
    template_name = "keys/keystatus_create.html"
    success_url = reverse_lazy("keystatus_list")

    def __init__(self, **kwargs):
        super(keystatusCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(keystatusCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keystatusCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(keystatusCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(keystatusCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(keystatusCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(keystatusCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(keystatusCreateView, self).get_initial()

    def form_invalid(self, form):
        response = super(keystatusCreateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(keystatusCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(keystatusCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(keystatusCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keystatusCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("keys:keystatus_detail", args=(self.object.pk,))


class keystatusUpdateView(UpdateView):
    model = keystatus
    form_class = keystatusForm
    template_name = "keys/keystatus_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "keystatus"

    def __init__(self, **kwargs):
        super(keystatusUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keystatusUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keystatusUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(keystatusUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(keystatusUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(keystatusUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(keystatusUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(keystatusUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(keystatusUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(keystatusUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(keystatusUpdateView, self).get_initial()

    def form_invalid(self, form):
        response = super(keystatusUpdateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(keystatusUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(keystatusUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(keystatusUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(keystatusUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keystatusUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("keys:keystatus_detail", args=(self.object.pk,))


class keystatusDeleteView(DeleteView):
    model = keystatus
    template_name = "keys/keystatus_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "keystatus"

    def __init__(self, **kwargs):
        super(keystatusDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keystatusDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(keystatusDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(keystatusDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(keystatusDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(keystatusDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(keystatusDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(keystatusDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(keystatusDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(keystatusDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keystatusDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("keys:keystatus_list")

@permission_required("admin.can_add_log_entry")
def keystatus_deleteAll(request):
    template = "keys/keystatus_deleteAll.html"

    prompt = {
        'warning': 'Once deleted, you will not be able to retrieve any of the records. Ensure that you are absolutely sure about you decition before you delete.'}

    if request.method == "GET":
        return render(request, template, prompt)

    keystatus.objects.all().delete()
    response = redirect('/keys/keystatus/')
    return response