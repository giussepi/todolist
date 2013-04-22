# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from todo.models import Todo


class TodoResource(ModelResource):
    class Meta:
        queryset = Todo.objects.all()
        # allowed_methods = ['get']
        resource_name = 'todo'
        authorization = Authorization()
