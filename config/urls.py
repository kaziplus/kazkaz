"""dumachallenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.kazi import forms as kazi_forms
from apps.accounts import forms as accounts_forms
from apps.accounts import views as accounts_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #url(r'^accounts/signup/seeker$', 'userena.views.signup', {'signup_form': accounts_forms.JobSeekerProfileForm,
    #    'extra_context': {'userform':accounts_forms.UserForm}}),


    url(r'^accounts/login/$', 'userena.views.signin'),
    url(r'^accounts/logout/$', 'userena.views.signout'),

    # url(r'^accounts/', include('userena.urls')),
    url(r'^', include('apps.kazi.urls')),
    url(r'^', include('apps.accounts.urls')),
]
