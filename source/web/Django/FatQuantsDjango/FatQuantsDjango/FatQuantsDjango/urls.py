"""
Definition of urls for FatQuantsDjango.
"""

from datetime import datetime
from django.conf.urls import url
from django.contrib.auth import views as auth_views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [

    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='useraccounts/login.html'), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='useraccounts/logout.html'), name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^admin/doc/', django.contrib.admindocs.urls),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
]
