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

from apps.accounts.models import JobSkill, RecruiterProfile
from apps.kazi.models import JobProfile
# ============================================================================
# useful constants
# ============================================================================
LEVELS = ('Nv','In','Ex')
SKILLS = ('Java', 'JavaScript', 'Haskell', 'Python', 'C', 'C++', 'Scala',
          'Clojure', 'Django')
TITLES = ('Developer', 'Programmer', 'Guru')
EXPERIENCE = list(range(15))
INDUSTRIES = ('CLH', 'CLL', 'CLM', 'DEH', 'DEL', 'DEM', 'DVH', 'DVL', 'DVM',
              'ITH', 'ITL', 'ITM', 'MOH', 'MOL', 'MOM', 'WDH', 'WDL', 'WDM')
EDU = ('DP', 'Bsc', 'Msc', 'Phd')
LOCATIONS = ('KsmH', 'KsmL', 'KsmM', 'MbsH', 'MbsL', 'MbsM', 'NkuH', 'NkuL',
             'NkuM', 'NrbH','NrbL', 'NrbM', 'NyrH', 'NyrL', 'NyrM', 'ThkH',
             'ThkL', 'ThkM')
GENDERS = ('MH', 'FH', 'MM', 'FM', 'ML', 'FL')
MIN_AGE = list(range(20,30))
MAX_AGE = list(range(45, 65))
RECRUITERS = RecruiterProfile.objects.all()
JOBSKILLS = JobSkill.objects.all()
# ============================================================================
# autofixture classes
# ============================================================================
class JobProfileAutoFixture(AutoFixture):
    """AutoFixture class for the JobProfile model

    It generates test data for the JobProfile Model
    The field_values is a  dictionary with field names of model as keys.

    """


    class Values:
        title = generators.ChoicesGenerator(values=TITLES)
        desc = 'About Job Seeker'
        gender = generators.ChoicesGenerator(values=GENDERS)
        owner = generators.ChoicesGenerator(values=RECRUITERS)
        industry = generators.ChoicesGenerator(values=INDUSTRIES)
        location = generators.ChoicesGenerator(values=LOCATIONS)
        skills = generators.ChoicesGenerator(values=JOBSKILLS)
        experience = random.choice(EXPERIENCE)
        min_age = generators.ChoicesGenerator(values=MIN_AGE)
        max_age = generators.ChoicesGenerator(values=MAX_AGE)
        edu = generators.ChoicesGenerator(values=EDU)

# ============================================================================
# autofixture registration
# ============================================================================
register(JobProfile, JobProfileAutoFixture)

# ============================================================================
# EOF
# ============================================================================
