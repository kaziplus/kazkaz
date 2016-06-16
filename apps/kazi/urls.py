"""
urls

"""
from django.conf.urls import url
from django.views.generic.base import TemplateView


from apps.kazi import views as kazi_views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),

    url(r'jobs/add/$', kazi_views.JobProfileCreate.as_view(), name='job-add'),
    url(r'jobs/(?P<pk>[0-9]+)/$', kazi_views.JobProfileUpdate.as_view(), name='job-update'),
    url(r'jobs/detail/(?P<pk>[0-9]+)/$', kazi_views.JobProfileDetail.as_view(), name='job-detail'),
    url(r'jobs/(?P<pk>[0-9]+)/delete/$', kazi_views.JobProfileDelete.as_view(), name='job-delete'),
    url(r'jobs/', kazi_views.JobProfileList.as_view(), name='job-prof-list'),

    url(r'matches/(?P<pk>[0-9]+)/$', kazi_views.JobMatchUpdate.as_view(), name='match-update'),
    url(r'matches/(?P<pk>[0-9]+)/$', kazi_views.JobMatchDetail.as_view(), name='match-detail'),
    url(r'matches/(?P<pk>[0-9]+)/delete/$', kazi_views.JobMatchDelete.as_view(), name='match-delete'),
    url(r'matches/', kazi_views.JobMatchList.as_view(), name='match-list'),

]
