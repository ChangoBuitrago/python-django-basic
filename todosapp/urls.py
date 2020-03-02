from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^todos/', include('todos.urls', namespace='todos')),
    url(r'^admin/', include(admin.site.urls)),
]