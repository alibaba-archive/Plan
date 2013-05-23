# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import *

class TaskAdmin(admin.StackedInline):
	model = Task
	extra = 3

class TLAdmin(admin.ModelAdmin):
	inlines = [TaskAdmin]
	list_display = ('category','duedate', 'created_at')


admin.site.register(Tasklist, TLAdmin)
