"""forms

"""
# ============================================================================
# necessary imports
# ============================================================================
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from apps.kazi.models import JobProfile


# ============================================================================
# model form classes
# ============================================================================
class JobProfileForm(ModelForm):
    """Job Profile web form class

    """
    class Meta:
        """nested meta class

        """
        model = JobProfile
        exclude = ['created', 'owner', 'score']
        help_texts = {'experience': _("experience in years.")}
# ============================================================================
# EOF
# ============================================================================
