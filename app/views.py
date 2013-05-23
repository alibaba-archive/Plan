#-*- coding: utf-8 -*-

from datetime import date
from .models import *
from django.shortcuts import render_to_response

from django.db import connection

def month(request):

	# current year
	d = date.today()
	year = d.year

	tls = Tasklist.objects.filter(duedate__year=year)

	group_by_month = {}
	for i in range(13):
		group_by_month[i] = []

	for tl in tls:
		month = tl.duedate.month
		data = group_by_month.get(month)
		data.append(tl)

	return render_to_response('index.jade', { "tasklists": group_by_month })