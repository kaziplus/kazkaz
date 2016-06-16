from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from apps.accounts.forms import UserForm, JobSeekerProfileForm, RecruiterProfileForm
from apps.accounts.models import RecruiterProfile
from apps.kazi.models import JobProfile

# Create your views here.

class JobSeekerProfileCreate(FormView):
    """create view

    """
    template_name = 'userena/signup_form.html'
    form_class = JobSeekerProfileForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(JobSeekerProfileCreate, self).get_context_data(**kwargs)
        context['userform'] = UserForm
        context['usertype'] = 'Job Seeker'

        return context

    def form_valid(self, form):
        """

        """
        user_form = UserForm(data=self.request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = JobSeekerProfileForm(data=self.request.POST).save(commit=False)
            profile.user = user
            profile.save()
        else:
            print(user_form.errors)



        return super(JobSeekerProfileCreate, self).form_valid(form)

class RecruiterProfileCreate(FormView):
    """create view

    """
    template_name = 'userena/signup_form.html'
    form_class = RecruiterProfileForm
    success_url = reverse_lazy('recruiter-profile')

    def get_context_data(self, **kwargs):
        context = super(RecruiterProfileCreate, self).get_context_data(**kwargs)
        context['userform'] = UserForm
        context['usertype'] = 'Recruiter'

        return context

    def form_valid(self, form):
        """

        """
        user_form = UserForm(data=self.request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = RecruiterProfileForm(data=self.request.POST).save(commit=False)
            profile.user = user
            profile.save()
        else:
            print(user_form.errors)



        return super(RecruiterProfileCreate, self).form_valid(form)

class RecruiterProfileDetail(LoginRequiredMixin, TemplateView):
    """Recruiter profile detail view

    """
    template_name = 'userena/profile_detail.html'

    def get_context_data(self, **kwargs):
        """overridden to add extra context

        """
        context = super(RecruiterProfileDetail, self).get_context_data(**kwargs)
        context['profile'] = RecruiterProfile.objects.filter(user=self.request.user)
        context['job_list'] = JobProfile.objects.filter(owner=context['profile'])

        return context
