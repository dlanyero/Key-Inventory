from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import building
from ..forms import buildingForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
#from braces import SuperuserRequiredMixin


class buildingListView(ListView):
    model = building
    template_name = "keys/building_list.html"
    paginate_by = 20
    context_object_name = "building_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 4

    def __init__(self, **kwargs):
        super(buildingListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(buildingListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(buildingListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(buildingListView, self).get_queryset()

    def get_allow_empty(self):
        return super(buildingListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(buildingListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(buildingListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(buildingListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(buildingListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(buildingListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(buildingListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(buildingListView, self).get_template_names()


class buildingDetailView(DetailView):
    model = building
    template_name = "keys/building_detail.html"
    context_object_name = "building"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        super(buildingDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(buildingDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(buildingDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(buildingDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(buildingDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(buildingDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(buildingDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(buildingDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(buildingDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(buildingDetailView, self).get_template_names()


class buildingCreateView(CreateView):
    model = building
    form_class = buildingForm
    template_name = "keys/building_create.html"
    success_url = reverse_lazy("building_list")

    def __init__(self, **kwargs):
        super(buildingCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(buildingCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(buildingCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(buildingCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(buildingCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(buildingCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(buildingCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(buildingCreateView, self).get_initial()

    def form_invalid(self, form):
        response = super(buildingCreateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(buildingCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(buildingCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(buildingCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(buildingCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("keys:building_detail", args=(self.object.pk,))


class buildingUpdateView(UpdateView):
    model = building
    form_class = buildingForm
    template_name = "keys/building_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "building"

    def __init__(self, **kwargs):
        super(buildingUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(buildingUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(buildingUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(buildingUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(buildingUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(buildingUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(buildingUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(buildingUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(buildingUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(buildingUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(buildingUpdateView, self).get_initial()

    def form_invalid(self, form):
        response = super(buildingUpdateView, self).form_invalid(form)
        response.status_code = 400
        return response

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(buildingUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(buildingUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(buildingUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(buildingUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(buildingUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("keys:building_detail", args=(self.object.pk,))


class buildingDeleteView(DeleteView):
    model = building
    template_name = "keys/building_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "building"

    def __init__(self, **kwargs):
        super(buildingDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(buildingDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(buildingDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(buildingDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(buildingDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(buildingDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(buildingDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(buildingDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(buildingDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(buildingDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(buildingDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("keys:building_list")

@permission_required("admin.can_add_log_entry")
def building_deleteAll(request):
    template = "keys/building_deleteAll.html"

    prompt = {
        'warning': 'Once deleted, you will not be able to retrieve any of the records. Ensure that you are absolutely sure about you decition before you delete.'}

    if request.method == "GET":
        return render(request, template, prompt)

    building.objects.all().delete()
    response = redirect('/keys/building/')
    return response