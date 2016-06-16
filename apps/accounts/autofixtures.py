"""
Accounts app autofixtures module

The autofixture module contains a few shortcuts to make the creation of test
data as fast as possible.

More here: http://django-autofixture.readthedocs.org/en/latest/usage.html

__author__ = 'Matt Gathu'
__date__ = 'June 2016'

"""
# ============================================================================
# necessary imports
# ============================================================================
import random
import datetime
from autofixture import generators, register, AutoFixture
# from autofixture.autofixtures import UserFixture

from apps.accounts.models import JobSkill, User, JobSeekerProfile

# ============================================================================
# useful constants
# ============================================================================
LEVELS = (('Nv', 'Novice'), ('In', 'Intermediate'), ('Ex', 'Expert'))
SKILLS = ('Java', 'JavaScript', 'Haskell', 'Python', 'C', 'C++', 'Scala',
          'Closure', 'Django')
EXPERIENCE = list(range(15))
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
# autofixture classes
# ============================================================================
class JobSkillAutoFixture(AutoFixture):
    """AutoFixture class for the JobSkill model

    It generates test data for the JobSkill Model
    The field_values is a  dictionary with field names of model as keys.

    """
    class Values:
        name = random.choice(SKILLS)
        about = 'About Skill'
        level = random.choice(LEVELS)

#class JobSeekerProfileAutoFixture(AutoFixture):
#    It generates test data for the JobSeekerProfile Model
#    The field_values is a  dictionary with field names of model as keys.
#
#    """
#    class Values:
#        about = 'About Job Seeker'
#        user = generators.InstanceGenerator(UserFixture)
#        dob = generators.DateGenerator(max_date=(datetime.date.today() - datetime.timedelta(365 * 20)))
#        mobile = '0702006545'
#        experience = random.choice(EXPERIENCE)
#        industry = random.choice(INDUSTRIES)
#        edu = random.choice(EDU)
#        gender = random.choice(GENDERS)
#        location = random.choice(LOCATIONS)
#        skills = random.choice(JobSkill.objects.all())

# ============================================================================
# autofixture registration
# ============================================================================
register(JobSkill, JobSkillAutoFixture)
# register(JobSeekerProfile, JobSeekerProfileAutoFixture)

# ============================================================================
# EOF
# ============================================================================
