# -*- coding: utf-8 -*-
""" todo's models """

from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Todo(models.Model):
    """ stores todo's data """
    title = models.CharField(max_length=150, blank=True)
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.title
    

    # def save(self):
    #     """  """
    #     try:
    #         obj = Todo.objects.get(title=self.title)
    #     except ObjectDoesNotExist:
    #         return super(self.__class__, self).save()
    #     else:
    #         obj
        
