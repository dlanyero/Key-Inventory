import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from ..models import building, keytype, key, keystatus, keyissue
from ..forms import buildingForm



@permission_required("admin.can_add_log_entry")
def reports(request):
    template = "reports/key_reports_base.html"
    return render(request, template)

@permission_required("admin.can_add_log_entry")
def keylocation_report(request):
    template = "reports/keylocation_report.html"

    if request.method == "GET":
        return render(request, template)

    key_id = request.POST['key_id']
    print(key_id)
    # You a are going to have more than one form value like it or not.
    # You may need to handle this alittle bit later. Look into the possibility of doing the right thing.
    data_set = keyissue.objects.get(key_id=key_id)
    print(data_set.key_id)

    current_owner = data_set.ownder_id
    date_issued = data_set.start_date
    return_date = data_set.End_date
    person_responsible = data_set.person_id
    content= {'owner' : current_owner, 'date': date_issued, 'return' : return_date, 'person' : person_responsible}
    context = {'content':content}
    return render(request,template, context)

@permission_required("admin.can_add_log_entry")
def keyuser_report(request):
    template = "reports/keyuser_report.html"

    if request.method == "GET":
        return render(request, template)

    person_id = request.POST['person_id']
    print(person_id)
    # You a are going to have more than one form value like it or not.
    data_set = keyissue.objects.filter(ownder_id = person_id)
    print(data_set[1])
    context = {'data':data_set}
    return render(request, template, context)
    #Loop through every value in the context from the template and place the values inside a table and then show the table.

