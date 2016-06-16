"""forms

"""
# ============================================================================
# necessary imports
# ============================================================================
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from apps.accounts.models import JobSeekerProfile, RecruiterProfile, User


# ============================================================================
# model form classes
# ============================================================================
class UserForm(ModelForm):
    """User model form

    """
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        """nested meta class

        """
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class JobSeekerProfileForm(ModelForm):
    """Job Seeker Profile web form class

    """
    class Meta:
        """nested meta class

        """
        model = JobSeekerProfile
        exclude = ['user', 'privacy', 'mugshot']
        help_texts = { 'dob': _('e.g.2006-10-25'), 'experience': _('Experience in years.')}


class RecruiterProfileForm(ModelForm):
    """Recruiter Profile web form class

    """
    class Meta:
        """nested meta class

        """
        model = RecruiterProfile
        exclude = ['user', 'privacy', 'mugshot']
# ============================================================================
# EOF
# ============================================================================
