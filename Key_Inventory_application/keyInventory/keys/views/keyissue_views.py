from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import keyissue
from ..forms import keyissueForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
#from braces import SuperuserRequiredMixin


class keyissueListView(ListView):
    model = keyissue
    template_name = "keys/keyissue_list.html"
    paginate_by = 20
    context_object_name = "keyissue_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        super(keyissueListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keyissueListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keyissueListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(keyissueListView, self).get_queryset()

    def get_allow_empty(self):
        return super(keyissueListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(keyissueListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(keyissueListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(keyissueListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(keyissueListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(keyissueListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(keyissueListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keyissueListView, self).get_template_names()


class keyissueDetailView(DetailView):
    model = keyissue
    template_name = "keys/keyissue_detail.html"
    context_object_name = "keyissue"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        super(keyissueDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keyissueDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keyissueDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(keyissueDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(keyissueDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(keyissueDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(keyissueDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(keyissueDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(keyissueDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keyissueDetailView, self).get_template_names()


class keyissueCreateView(CreateView):
    model = keyissue
    form_class = keyissueForm
    template_name = "keys/keyissue_create.html"
    success_url = reverse_lazy("keyissue_list")

    def __init__(self, **kwargs):
        super(keyissueCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(keyissueCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keyissueCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(keyissueCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(keyissueCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(keyissueCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(keyissueCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(keyissueCreateView, self).get_initial()

    def form_invalid(self, form):
        response = super(keyissueCreateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(keyissueCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(keyissueCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(keyissueCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keyissueCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("keys:keyissue_detail", args=(self.object.pk,))


class keyissueUpdateView(UpdateView):
    model = keyissue
    form_class = keyissueForm
    template_name = "keys/keyissue_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "keyissue"

    def __init__(self, **kwargs):
        super(keyissueUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keyissueUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(keyissueUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(keyissueUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(keyissueUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(keyissueUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(keyissueUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(keyissueUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(keyissueUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(keyissueUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(keyissueUpdateView, self).get_initial()

    def form_invalid(self, form):
        response = super(keyissueUpdateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(keyissueUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(keyissueUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(keyissueUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(keyissueUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keyissueUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("keys:keyissue_detail", args=(self.object.pk,))


class keyissueDeleteView(DeleteView):
    model = keyissue
    template_name = "keys/keyissue_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "keyissue"

    def __init__(self, **kwargs):
        super(keyissueDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(keyissueDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(keyissueDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(keyissueDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(keyissueDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(keyissueDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(keyissueDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(keyissueDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(keyissueDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(keyissueDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(keyissueDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("keys:keyissue_list")


@permission_required("admin.can_add_log_entry")
def keyissue_deleteAll(request):
    template = "keys/keyissue_deleteAll.html"

    prompt = {
        'warning': 'Once deleted, you will not be able to retrieve any of the records. Ensure that you are absolutely sure about you decition before you delete.'}

    if request.method == "GET":
        return render(request, template, prompt)

    keyissue.objects.all().delete()
    response = redirect('/keys/keyissue/')
    return response