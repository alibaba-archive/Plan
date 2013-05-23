#_*_ coding: utf-8 _*_

from django.conf import settings
from django.contrib import admin
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

admin.autodiscover()
urlpatterns = patterns('',
	# 管理后台
	(r'^admin/', include(admin.site.urls)),

	# 静态文件
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './media/'}),
	(r'^$', 'app.views.month'),
)
handler404 = 'page.views.custom_404_view'
handler500 = 'page.views.custom_500_view'
