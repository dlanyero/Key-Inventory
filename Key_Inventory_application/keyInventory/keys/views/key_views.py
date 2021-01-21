from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import key
from ..forms import keyForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
#from braces import SuperuserRequiredMixin


class keyListView(ListView):
    model = key
    template_name = "keys/key_list.html"
    paginate_by = 20
    context_object_name = "key_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        super(keyListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keyListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keyListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(keyListView, self).get_queryset()

    def get_allow_empty(self):
        return super(keyListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(keyListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(keyListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(keyListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(keyListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(keyListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(keyListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keyListView, self).get_template_names()


class keyDetailView(DetailView):
    model = key
    template_name = "keys/key_detail.html"
    context_object_name = "key"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        super(keyDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keyDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keyDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(keyDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(keyDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(keyDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(keyDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(keyDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(keyDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keyDetailView, self).get_template_names()


class keyCreateView(CreateView):
    model = key
    form_class = keyForm
    template_name = "keys/key_create.html"
    success_url = reverse_lazy("key_list")

    def __init__(self, **kwargs):
        super(keyCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(keyCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keyCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(keyCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(keyCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(keyCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(keyCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(keyCreateView, self).get_initial()

    def form_invalid(self, form):
        response = super(keyCreateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(keyCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(keyCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(keyCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keyCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("keys:key_detail", args=(self.object.pk,))


class keyUpdateView(UpdateView):
    model = key
    form_class = keyForm
    template_name = "keys/key_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "key"

    def __init__(self, **kwargs):
        super(keyUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keyUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keyUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(keyUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(keyUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(keyUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(keyUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(keyUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(keyUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(keyUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(keyUpdateView, self).get_initial()

    def form_invalid(self, form):
        response = super(keyUpdateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(keyUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(keyUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(keyUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(keyUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keyUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("keys:key_detail", args=(self.object.pk,))


class keyDeleteView(DeleteView):
    model = key
    template_name = "keys/key_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "key"

    def __init__(self, **kwargs):
        super(keyDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keyDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(keyDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(keyDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(keyDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(keyDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(keyDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(keyDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(keyDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(keyDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keyDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("keys:key_list")\

@permission_required("admin.can_add_log_entry")
def key_deleteAll(request):
    template = "keys/key_deleteAll.html"

    prompt = {
        'warning': 'Once deleted, you will not be able to retrieve any of the records. Ensure that you are absolutely sure about you decition before you delete.'}

    if request.method == "GET":
        return render(request, template, prompt)

    key.objects.all().delete()
    response = redirect('/keys/keys/')
    return response

