# -*- coding: utf-8 -*-

from django.db import models


class Tasklist(models.Model):

	category_choices = (
		(0, 'Web'),
		(1, 'iOS'),
		(2, 'Android')
	)

	category = models.IntegerField(u"类别", default=0, choices=category_choices)
	duedate = models.DateField(u"截止日期",null=True, blank=True)
	created_at = models.DateTimeField(u'创建日期', auto_now=True, auto_now_add=True, null=True)
	description = models.CharField(u"描述", max_length=200, null=True, blank=True)

	def __unicode__(self):
		return self.get_category_display()

class Task(models.Model):
	
	tasklist = models.ForeignKey(Tasklist, verbose_name=u"所属列表", related_name="tasks")
	content = models.CharField(u"内容", max_length=50)
	description = models.CharField(u"描述", max_length=200, null=True, blank=True)
	order = models.IntegerField(u"序号", default=1)
	duedate = models.DateField(u"截止日期",null=True, blank=True)
	created_at = models.DateTimeField(u'创建日期', auto_now=True, auto_now_add=True, null=True)

	class Meta:
		ordering = ["order"]

	def __unicode__(self):
		return self.content