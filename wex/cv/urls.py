from django.conf.urls import url
from .views import HomeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
]
