# -*- coding: utf-8 -*-
""" todo's views """

from django.views.generic import TemplateView


class index(TemplateView):
    """ shows the main page with the todo SPA """
    template_name = 'todo/index.html'
