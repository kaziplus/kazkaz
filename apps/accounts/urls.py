"""
urls

"""
from django.conf.urls import url
from django.contrib.auth import views as auth_views


from apps.accounts import views as accounts_views

urlpatterns = [
    url(r'^accounts/signup/seeker$',accounts_views.JobSeekerProfileCreate.as_view()),
    # url(r'^accounts/profile/seeker/(?P<pk>[0-9]+)/$',accounts_views.RecruiterProfileCreate.as_view()),

    url(r'^accounts/signup/recruiter$',accounts_views.RecruiterProfileCreate.as_view()),
    url(r'^accounts/recruiter/$',accounts_views.RecruiterProfileDetail.as_view(), name='recruiter-profile'),

    # url(r'^accounts/login/$', auth_views.login),
]
