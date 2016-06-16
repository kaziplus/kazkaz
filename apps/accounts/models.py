"""models

"""
# ============================================================================
# necessary imports
# ============================================================================
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

# ============================================================================
# useful constants
#=============================================================================
EDU = sorted((
    ('DP', 'Diploma'),
    ('Bsc', "Bachelor's Degree"),
    ('Msc', "Master's Degree"),
    ('Phd', 'Post Graduate')
))

LOCATIONS = sorted((
    ('NrbH', 'Nairobi - High'),
    ('NkuH', 'Nakuru - High'),
    ('MbsH', 'Mombasa - High'),
    ('KsmH', 'Kisumu - High'),
    ('ThkH', 'Thika - High'),
    ('NyrH', 'Nyeri - High'),

    ('NrbM', 'Nairobi - Medium'),
    ('NkuM', 'Nakuru - Medium'),
    ('MbsM', 'Mombasa - Medium'),
    ('KsmM', 'Kisumu - Medium'),
    ('ThkM', 'Thika - Medium'),
    ('NyrM', 'Nyeri - Medium'),

    ('NrbL', 'Nairobi - Low'),
    ('NkuL', 'Nakuru - Low'),
    ('MbsL', 'Mombasa - Low'),
    ('KsmL', 'Kisumu - Low'),
    ('ThkL', 'Thika - Low'),
    ('NyrL', 'Nyeri - Low'),
))

INDUSTRIES = sorted((
    ('ITH', 'IT - High'),
    ('CLH', 'Cloud - High'),
    ('WDH', 'Web Development - High'),
    ('MOH', 'Mobile Development - High'),
    ('DEH', 'Desktop Development - High'),
    ('DVH', 'DevOps - High'),

    ('ITM', 'IT - Medium'),
    ('CLM', 'Cloud - Medium'),
    ('WDM', 'Web Development - Medium'),
    ('MOM', 'Mobile Development - Medium'),
    ('DEM', 'Desktop Development - Medium'),
    ('DVM', 'DevOps - Medium'),

    ('ITL', 'IT - Low'),
    ('CLL', 'Cloud - Low'),
    ('WDL', 'Web Development - Low'),
    ('MOL', 'Mobile Development - Low'),
    ('DEL', 'Desktop Development - Low'),
    ('DVL', 'DevOps - Low'),
))

GENDERS = sorted((
    ('MH', 'Male - High'),
    ('FH', 'Female - High'),

    ('MM', 'Male - Medium'),
    ('FM', 'Female - Medium'),

    ('ML', 'Male - Low'),
    ('FL', 'Female - Low'),
))
# ============================================================================
# model classes
# ============================================================================
class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True, verbose_name=_('user'),
                                related_name='user_profile',
                                on_delete=models.CASCADE)
    about = models.TextField()


class JobSeekerProfile(UserProfile):
    """Job Seeker Profile

    """
    dob = models.DateField('date of birth')
    mobile = models.CharField(max_length=20)
    experience = models.IntegerField()
    industry = models.CharField(max_length=100, choices=INDUSTRIES, default='IT')
    edu = models.CharField('Education Level', max_length=50, choices=EDU, default='DP')
    gender = models.CharField(max_length=50, choices=GENDERS, default='MM')
    location = models.CharField('Area of Residence', max_length=100, choices=LOCATIONS, default='Nrb')
    skills = models.ManyToManyField('JobSkill')

    @property
    def age(self):
        """Return full name

        """
        age = datetime.date.today() - self.dob
        age = int(age.days / 365)

        return age
    @property
    def get_industry(self):
        """Return industry

        """
        return self.get_industry_display()

    @property
    def get_location(self):
        """Return location

        """
        return self.get_location_display()

    @property
    def get_gender(self):
        """Return gender

        """
        return self.get_gender_display()

    @property
    def get_name(self):
        """Return full name

        """
        return self.user.last_name + self.user.first_name

    @property
    def get_skills(self):
        """Return skills

        """
        return ','.join(str(skill) for skill in self.skills.all())

    def compute_score(self, profile):
        """calculate seeker's score based on job profile

        """
        score = 0
        # ====================================================================
        # age consideration
        # ====================================================================
        if profile.max_age:
            if self.age < profile.max_age:
                score += 1
        if profile.min_age:
            if self.age > profile.min_age:
                score += 1
        # ====================================================================
        # skills consideration
        # ====================================================================
        for skill in profile.skills.all():
            if skill in self.skills.all():
                if skill.level == 'Ex':
                    score += 9
                elif skill.level == 'In':
                    score += 6
                else:
                    score += 3
        # ====================================================================
        # industry consideration
        # ====================================================================
        if profile.industry == self.industry:
            if profile.industry.endswith('H'):
                score += 3
            elif profile.industry.endswith('M'):
                score += 2
            else:
                score += 1
        # ====================================================================
        # location consideration
        # ====================================================================
        if profile.location == self.location:
            if profile.location.endswith('H'):
                score += 3
            elif profile.location.endswith('M'):
                score += 2
            else:
                score += 1
        # ====================================================================
        # gender consideration
        # ====================================================================
        if profile.gender == self.gender:
            if profile.gender.endswith('H'):
                score += 3
            elif profile.gender.endswith('M'):
                score += 2
            else:
                score += 1
        # ====================================================================
        # experience consideration
        # ====================================================================
        if (self.experience - profile.experience) >= 0:
            score += 3
        elif (self.experience - profile.experience) >= -2:
            score += 1

        # ====================================================================
        # education consideration
        # ====================================================================
        if profile.edu == 'DP':
            if self.edu in ('DP', 'BSc', 'Msc' , 'Phd'):
                score += 1
        elif profile.edu == 'Bsc':
            if self.edu in ('BSc', 'Msc' , 'Phd'):
                score += 2
        elif profile.edu == 'Msc':
            if self.edu in ('Msc' , 'Phd'):
                score += 4
        elif profile.edu == 'Phd':
            if self.edu == profile.edu:
                score += 8
        # =====================================================================
        # return total score
        # ====================================================================
        return score

    def __str__(self):
        """model repr

        """
        return 'job seeker'

class JobSkill(models.Model):
    """Job Skill Model

    """
    LEVELS = (('Nv', 'Novice'), ('In', 'Intermediate'), ('Ex', 'Expert'))

    name = models.CharField(max_length=50)
    about = models.CharField(max_length=255, blank=True)
    level = models.CharField('Level of Mastery', choices=LEVELS, max_length=50)

    class Meta:
        ordering = ['name', 'level']
        unique_together = (('name', 'level'),)

    def __str__(self):
        """model repr

        """
        return ' - '.join((self.name, self.get_level_display()))


class RecruiterProfile(UserProfile):
    """Recruiter Profile

    """
    company = models.CharField(max_length=100)

    def __str__(self):
        """model repr

        """
        return 'recruiter'
# ============================================================================
# EOF
# ============================================================================
