"""
generate matches command

"""
# ============================================================================
# necessary imports
# ============================================================================
import random
import datetime
from itertools import chain


from django.core.management.base import BaseCommand
from django.db import IntegrityError, transaction
from autofixture import generators


from apps.accounts.models import JobSkill, JobSeekerProfile, User, RecruiterProfile
from apps.kazi.models import JobProfile, JobMatch
from apps.kazi.core import filter_seekers

# ============================================================================
# command class
# ============================================================================
class Command(BaseCommand):
    """Scraping Command"""
    help = 'initialize scrapers by setting up tracking database entries'

    def handle(self, *args, **options):
        """run command"""
        jobs = JobProfile.objects.all()
        seekers  = JobSeekerProfile.objects.all()
        for job in jobs:
            cands = filter_seekers(seekers, job)
            match = JobMatch.objects.filter(recruiter=job.owner, job_profile=job).first()
            if not match:
                match = JobMatch(recruiter=job.owner, job_profile=job)
                match.save()
            match.job_seekers.clear()
            for cand in cands:
                match.job_seekers.add(seeker)
            match.save()
