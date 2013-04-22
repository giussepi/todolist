# -*- coding: utf-8 -*-
""" todo's urls """

from django.conf.urls import patterns, include, url
from todo.views import index

urlpatterns = patterns(
    '',
    url(r'^$', index.as_view(), name='home'),
)
