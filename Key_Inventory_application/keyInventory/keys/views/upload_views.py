from __future__ import print_function
import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from ..models import building, keytype, key, keystatus, keyissue

from ..forms import buildingForm


@permission_required("admin.can_add_log_entry")
def buildings_upload(request):
    template = "building_upload.html"

    prompt = {'order': 'The order of the csv should be ID, Name, Code, IsResidential, IsInactive, version '}

    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['building_csv_file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter='|', quotechar = ";"):
        _, created= building.objects.update_or_create(
            identifier=column[0],
            name=column[1],
            code=column[2],
            is_residential=column[3],
            is_inactive=column[4],
            version=column[5]
        )

    context = {}
    return render(request, template, context)

@permission_required("admin.can_add_log_entry")
def keytype_upload(request):
    template = "keytype_upload.html"

    prompt = {'order': 'The order of the csv should be ID, Code, Manu_Info, Description, BuildingID'}

    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['keytype_csv_file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter='|', quotechar = ";"):
        if column[4] == "":
            _, created = keytype.objects.update_or_create(
                identifier=column[0],
                code=column[1],
                manu_info=column[2],
                description=column[3]
            )
        else:
            _, created= keytype.objects.update_or_create(
                identifier=column[0],
                code=column[1],
                manu_info=column[2],
                description=column[3],
                building_id=building.objects.get(identifier=column[4])
            )
    context = {}
    return render(request, template, context)

@permission_required("admin.can_add_log_entry")
def key_upload(request):
    template = "key_upload.html"

    prompt = {'order': 'The order of the csv should be ID, Number, Code, Keytype_ID '}

    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['key_csv_file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter='|', quotechar = ";"):
        # Only the non empty columns are going to be added for now. Remember to think about what you would like to do about the empty ones later,
        if column[2] != "":
            _, created= key.objects.update_or_create(
                identifier=column[0],
                number=column[1],
                keytype_id = keytype.objects.get(identifier=column[2])
            )
        # Use try catch to handle this exception.

    context = {}
    return render(request, template, context)

@permission_required("admin.can_add_log_entry")
def keystatus_upload(request):
    template = "keystatus_upload.html"

    prompt = {'order': 'The order of the csv should be ID, label, order, is_active'}

    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['keystatus_csv_file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter='|', quotechar = ";"):
        _, created= keystatus.objects.update_or_create(
            identifier=column[0],
            label=column[1],
            order=column[2],
            is_active=column[3],
        )

    context = {}
    return render(request, template, context)

@permission_required("admin.can_add_log_entry")
def keyissue_upload(request):
    template = "keyissue_upload.html"

    prompt = {'order': 'The order of the csv should be ID, Name, Code, IsResidential, IsInactive, version '}

    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['keyissue_csv_file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter='|', quotechar = ";"):
        if column[1] != "" and column[2] != "":
            _, created= keyissue.objects.update_or_create(
                identifier=column[0],
                key_id= key.objects.get(identifier=column[1]),
                keystatus_id=keystatus.objects.get(identifier=column[2]),
                start_date=column[3],
                End_date=column[4],
                ownder_id=column[5],
                person_id = column[6],
                note=column[7]
            )
        #Find a sage way to notify the user incase there are exceptions on some rows regarding that constraint.

    context = {}
    return render(request, template, context)