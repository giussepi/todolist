from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from tastypie.api import Api
from todo.api.resources import TodoResource

v1_api = Api(api_name='v1')
v1_api.register(TodoResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todolist_project.views.home', name='home'),
    # url(r'^todolist_project/', include('todolist_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('todo.urls')),
    url(r'^api/', include(v1_api.urls)),
)
