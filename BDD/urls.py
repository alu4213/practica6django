from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    ('^pages/', include('django.contrib.flatpages.urls')),
    (r'^home', 'django.views.generic.simple.direct_to_template',
    {'template': '/home/alu4213/dsi/django_projects/BDD/mytemplates/home.html'}),
    (r'^help', 'django.views.generic.simple.direct_to_template',
    {'template': '/home/alu4213/dsi/django_projects/BDD/mytemplates/help.html'}),
    (r'^about', 'django.views.generic.simple.direct_to_template',
    {'template': '/home/alu4213/dsi/django_projects/BDD/mytemplates/about.html'}),
)

