# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from disa_app import views


admin.autodiscover()


urlpatterns = [

    ## primary app urls...
    url( r'^browse/$', views.browse, name='browse_url' ),
    url( r'^admin/', admin.site.urls ),  # eg host/project_x/admin/

    ## support urls...
    url( r'^version/$', views.version, name='version_url' ),
    url( r'^error_check/$', views.error_check, name='error_check_url' ),

    url( r'^$', RedirectView.as_view(pattern_name='browse_url') ),

    # url( r'^admin/login/', RedirectView.as_view(pattern_name='login_url') ),
    # url( r'^login/$', views.login, name='login_url' ),

    ]
