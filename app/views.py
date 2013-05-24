#-*- coding: utf-8 -*-

from datetime import date
from .models import *
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def month(request):

	d = date.today()
	tls = Tasklist.objects.filter(duedate__year=d.year)

	group_by_month = {}
	for i in range(13):
		group_by_month[i] = []

	index = {
		'web' : 0,
		'ios' : 1,
		'android' : 2
	}
	for tl in tls:
		month = tl.duedate.month
		data = group_by_month.get(month)
		i = index.get(tl.get_category_display().lower())
		data.insert(i, tl)

	return render_to_response('index.jade', { "tasklists": group_by_month })