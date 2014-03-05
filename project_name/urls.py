from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html")),

    #apps
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^news/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    #url(r'^photologue/', include('photologue.urls')),

    #admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/util/tools/', include('admin_tools.urls')),

    #cms
    url(r'^', include('cms.urls')),
)
