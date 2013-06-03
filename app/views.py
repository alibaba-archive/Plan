#-*- coding: utf-8 -*-

from datetime import date
from .models import *
from django.shortcuts import render_to_response
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

INDEX = {
    'web' : 0,
    'ios' : 1,
    'android' : 2,
    'server': 3,
    'ui': 4
}

def construct(lists):
    group_by_month = {}
    for i in range(13):
        group_by_month[i] = []

    for tl in lists:
        month = tl.duedate.month
        data = group_by_month.get(month)
        i = INDEX.get(tl.get_category_display().lower())
        data.insert(i, tl)
    return group_by_month


@login_required
def month(request):

    d = date.today()
    tls = Tasklist.objects.filter(duedate__year=d.year, project__isnull=True)
    group_by_month = construct(tls)
    return render_to_response('index.jade', { "tasklists": group_by_month })

def lists(request, project_attr=None):

    if not project_attr:
        return HttpResponseBadRequest('Bad')

    try:
        project_id = int(project_attr)
        project_name = None
    except:
        project_id = None
        project_name = project_attr

    category = request.REQUEST.get('cg', None)

    conditions = {}
    if project_id: conditions['project__pk'] = project_id
    if project_name: conditions['project__name'] = project_name
    if category:
        try:
            conditions['category'] = int(category)
        except:
            conditions['category'] = INDEX.get(category, '4')
    tls = Tasklist.objects.filter(**conditions)
    group_by_month = construct(tls)
    return render_to_response('index.jade', { "tasklists": group_by_month })


