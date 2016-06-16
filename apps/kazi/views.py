"""

"""
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from apps.kazi.models import JobProfile, JobMatch
from apps.kazi.forms import JobProfileForm
from apps.accounts.forms import JobSeekerProfileForm, RecruiterProfileForm
from apps.accounts.models import RecruiterProfile, JobSeekerProfile


# ============================================================================
# class based views
# ============================================================================
class JobProfileCreate(LoginRequiredMixin, CreateView):
    """create view

    """
    model = JobProfile
    form_class = JobProfileForm
    success_url = reverse_lazy('recruiter-profile')

    def form_valid(self, form):
        """overridden to add user

        """
        form.instance.owner = RecruiterProfile.objects.filter(user=self.request.user).first()
        return super(JobProfileCreate, self).form_valid(form)


class JobProfileDetail(LoginRequiredMixin, DetailView):
    """detail view

    """
    template_name = 'kazi/jobprofile_detail.html'
    model = JobProfile

    def get_context_data(self, **kwargs):
        """overridden to add extra context

        """
        context = super(JobProfileDetail, self).get_context_data(**kwargs)

        profile = self.get_object()
        jobmatch = JobMatch.objects.filter(job_profile=profile).last()
        cands = jobmatch.job_seekers.all()
        for cand in cands:
            cand.score = cand.compute_score(profile)
        cands = reversed(cands)
        context['job'] = profile
        context['jobmatch'] = jobmatch
        context['recruiter'] = RecruiterProfile.objects.filter(user=self.request.user)
        context['candidates'] = cands

        return context



class JobProfileUpdate(LoginRequiredMixin, UpdateView):
    """update view

    """
    model = JobProfile
    form_class = JobProfileForm
    success_url = reverse_lazy('recruiter-profile')


class JobProfileDelete(LoginRequiredMixin, DeleteView):
    """delete view

    """
    model = JobProfile
    success_url = reverse_lazy('recruiter-profile')


class JobProfileList(LoginRequiredMixin, ListView):
    """list view

    """
    context_object_name = 'job_profile_list'

    def get_queryset(self):
        recruiter = RecruiterProfile.objects.filter(user=self.request.user)
        return JobProfile.objects.filter(owner=recruiter)

class JobProfileFormView(LoginRequiredMixin, FormView):
    """form view

    """
    form_class = JobProfileForm
    success_url = reverse_lazy('job-prof-list')

    def form_valid(self, form):
        """when valid form data is POSTed

        """
        return super(JobProfileFormView, self).form_valid(form)


class JobMatchList(LoginRequiredMixin, ListView):
    """list view

    """
    context_object_name = 'job_match_list'

    def get_queryset(self):
        recruiter = RecruiterProfile.objects.filter(user=self.request.user)
        return JobMatch.objects.filter(recruiter=recruiter)


class JobMatchDetail(LoginRequiredMixin, DetailView):
    """detail view

    """
    model = JobMatch

class JobMatchUpdate(LoginRequiredMixin, UpdateView):
    """update view

    """
    model = JobMatch



class JobMatchDelete(LoginRequiredMixin, DeleteView):
    """delete view

    """
    model = JobMatch
    success_url = reverse_lazy('recruiter-profile')
# ============================================================================
# EOF
# ============================================================================
