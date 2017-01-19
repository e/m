from django.conf.urls import url, include
from django.contrib import admin
from cv import urls as cv_urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', include(cv_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
