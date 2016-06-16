"""models

"""
# ============================================================================
# necessary imports
# ============================================================================
from django.db import models
from django.db.models.signals import pre_save, post_save


from apps.accounts.models import JobSeekerProfile, LOCATIONS, INDUSTRIES, GENDERS, EDU
from apps.kazi.core import filter_seekers
# ============================================================================
# utility fuctions
#=============================================================================
def compute_job_score(sender, instance, **kwargs):
    """computer job score before saving

    """
    try:
        instance.score = instance.compute_score()
    except ValueError:
        pass

def generate_match(sender, instance, **kwargs):
    """

    """
    print('generating match')
    recruiter = instance.owner
    try:
        job_seekers = filter_seekers(JobSeekerProfile.objects.all(), instance)
    except ValueError:
        pass
    else:
        match = JobMatch.objects.filter(recruiter=recruiter, job_profile=instance).first()
        if not match:
            match = JobMatch(recruiter=recruiter, job_profile=instance)
            match.save()
        match.job_seekers.clear()
        for seeker in job_seekers:
            match.job_seekers.add(seeker)
        match.save()
# ============================================================================
# model classes
# ============================================================================
class JobMatch(models.Model):
    """Job Match

    """
    recruiter = models.ForeignKey('accounts.RecruiterProfile', on_delete=models.CASCADE)
    job_profile = models.ForeignKey('JobProfile', on_delete=models.CASCADE)
    job_seekers = models.ManyToManyField('accounts.JobSeekerProfile')

    def __str__(self):
        """model repr

        """
        return self.job_profile.title + 'matches'


class JobProfile(models.Model):
    """Job Profile

    """
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    gender = models.CharField('Gender with Priority', max_length=50, choices=GENDERS, default='FH')
    owner = models.ForeignKey('accounts.RecruiterProfile', on_delete=models.CASCADE)
    industry = models.CharField('Industry with Priority', max_length=100, choices=INDUSTRIES, default='ITM')
    location = models.CharField('Location with Priority', max_length=100, choices=LOCATIONS, default='NrbH')
    skills = models.ManyToManyField('accounts.JobSkill')
    experience = models.IntegerField('Minimum Experience')
    min_age = models.IntegerField('Minimum Age', blank=True, null=True)
    max_age = models.IntegerField('Maximum Age', blank=True, null=True)
    score = models.IntegerField('Score', blank=True, null=True)
    edu = models.CharField('Minimum Education Level', choices=EDU, max_length=50, default='Bsc')

    @property
    def get_location(self):
        """Return location

        """
        return self.get_location_display()

    @property
    def get_industry(self):
        """Return industry

        """
        return self.get_industry_display()

    @property
    def get_gender(self):
        """Return gender

        """
        return self.get_gender_display()

    @property
    def get_skills(self):
        """Return skills

        """
        return ','.join(str(skill) for skill in self.skills.all())

    def compute_score(self):
        """Get total job profile score based on attributes

        """
        score = 0

        # ====================================================================
        # age consideration
        # ====================================================================
        if self.max_age:
            score += 1
        if self.min_age:
            score += 1

        # ====================================================================
        # skills consideration
        # ====================================================================
        for skill in self.skills.all():
            if skill.level == 'Ex':
                score += 9
            elif skill.level == 'In':
                score += 6
            else:
                score += 3
        # ====================================================================
        # industry consideration
        # ====================================================================
        if self.industry.endswith('H'):
            score += 3
        elif self.industry.endswith('M'):
            score += 2
        else:
            score += 1

        # ====================================================================
        # location consideration
        # ====================================================================
        if self.location.endswith('H'):
            score += 3
        elif self.location.endswith('M'):
            score += 2
        else:
            score += 1

        # ====================================================================
        # gender consideration
        # ====================================================================
        if self.gender.endswith('H'):
            score += 3
        elif self.gender.endswith('M'):
            score += 2
        else:
            score += 1

        # ====================================================================
        # experience consideration
        # ====================================================================
        if self.experience:
            score += 3

        # ====================================================================
        # education consideration
        # ====================================================================
        if self.edu == 'DP':
            score += 1
        elif self.edu == 'Bsc':
            score += 2
        elif self.edu == 'Msc':
            score += 4
        else:
            score += 8
        # =====================================================================
        # return total score
        # ====================================================================
        return score

    @property
    def matches(self):
        """Get number of job seekers matched to this Profile

        """
        # Default value
        matches = 0

        job_match =  JobMatch.objects.filter(job_profile=self).first()
        if job_match:
            matches = job_match.job_seekers.count()

        return matches

    class Meta:
        ordering = ['title']
        unique_together = (('title', 'owner'),)

    def __str__(self):
        """model repr

        """
        return self.title

# ============================================================================
# hook up post_save signal to reciever
# ============================================================================
post_save.connect(generate_match, sender=JobProfile, dispatch_uid="generate_matches")
pre_save.connect(compute_job_score, sender=JobProfile, dispatch_uid='compute_score')

# ============================================================================
# EOF
# ============================================================================
