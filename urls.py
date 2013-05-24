#_*_ coding: utf-8 _*_

from django.conf import settings
from django.contrib import admin
from django.conf.urls import *

admin.autodiscover()
urlpatterns = patterns('',
	# 管理后台
	(r'^admin/', include(admin.site.urls)),

	# 静态文件
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './media/'}),
	(r'^$', 'app.views.month'),
	(r'^login/?', 'django.contrib.auth.views.login', {'template_name': 'login.jade'}),
	(r'^logout/?', 'django.contrib.auth.views.logout', {'next_page': '/login'}),
)
handler404 = 'page.views.custom_404_view'
handler500 = 'page.views.custom_500_view'
