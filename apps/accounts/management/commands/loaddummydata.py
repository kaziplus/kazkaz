"""
dummy data set up command

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
from apps.kazi.models import JobProfile

# ============================================================================
# useful constants
# ============================================================================
DATES = ((1996, 6, 15),(1991, 6, 15),(1981, 6, 15),(1971, 6, 15),(1966, 6, 15))
GENDERS = ['FH', 'FL', 'FM', 'MH', 'ML', 'MM']
INDUSTRIES = ['CLH', 'CLL', 'CLM', 'DEH', 'DEL', 'DEM', 'DVH', 'DVL', 'DVM',
              'ITH', 'ITL', 'ITM', 'MOH', 'MOL', 'MOM', 'WDH', 'WDL', 'WDM']

LOCATIONS = ['KsmH', 'KsmL', 'KsmM', 'MbsH', 'MbsL', 'MbsM', 'NkuH', 'NkuL',
             'NkuM', 'NrbH', 'NrbL', 'NrbM', 'NyrH', 'NyrL', 'NyrM', 'ThkH',
             'ThkL', 'ThkM']
EDU = ['Bsc', 'DP', 'Msc', 'Phd']
ABOUT = 'About Skill'
LEVELS = ('Nv', 'In', 'Ex')
SKILLS = ('Java', 'JavaScript', 'Haskell', 'Python', 'C', 'C++', 'Scala',
          'Closure', 'Django')
TITLES = ('Developer', 'Programmer', 'Guru')
MALE_NAMES = [
        'Abraham', 'Adam', 'Anthony', 'Brian', 'Bill', 'Ben', 'Calvin',
        'David', 'Daniel', 'George', 'Henry', 'Isaac', 'Ian', 'Jonathan',
        'Jeremy', 'Jacob', 'John', 'Jerry', 'Joseph', 'James', 'Larry',
        'Michael', 'Mark', 'Paul', 'Peter', 'Phillip', 'Stephen', 'Tony',
        'Titus', 'Trevor', 'Timothy', 'Victor', 'Vincent', 'Winston', 'Walt']
FEMALE_NAMES = [
        'Abbie', 'Anna', 'Alice', 'Beth', 'Carrie', 'Christina', 'Danielle',
        'Emma', 'Emily', 'Esther', 'Felicia', 'Grace', 'Gloria', 'Helen',
        'Irene', 'Joanne', 'Joyce', 'Jessica', 'Kathy', 'Katie', 'Kelly',
        'Linda', 'Lydia', 'Mandy', 'Mary', 'Olivia', 'Priscilla',
        'Rebecca', 'Rachel', 'Susan', 'Sarah', 'Stacey', 'Vivian']
SURNAMES = [
        'Smith', 'Walker', 'Conroy', 'Stevens', 'Jones', 'Armstrong',
        'Johnson', 'White', 'Stone', 'Strong', 'Olson', 'Lee', 'Forrest',
        'Baker', 'Portman', 'Davis', 'Clark', 'Brown', 'Roberts', 'Ellis',
        'Jackson', 'Marshall', 'Wang', 'Chen', 'Chou', 'Tang', 'Huang', 'Liu',
        'Shih', 'Su', 'Song', 'Yang', 'Chan', 'Tsai', 'Wong', 'Hsu', 'Cheng',
        'Chang', 'Wu', 'Lin', 'Yu', 'Yao', 'Kang', 'Park', 'Kim', 'Choi',
        'Ahn', 'Mujuni']
PASSWORD = 'password'
EMAIL_GENERATOR = generators.EmailGenerator()
RECRUITERS  = [('Smith', 'Abraham'), ('Walker', 'Adam'), ('Conroy', 'Anthony'),
              ('Stevens', 'Brian')]
COMPANIES = ['Giggler', 'Microhard', 'Headpage', 'Chatsnap', 'Bookface', 'Boxdrop']

def generate_title():
    return ' '.join((random.choice(SKILLS), random.choice(TITLES)))

def save_model(model):
    try:
        with transaction.atomic():
            model.save()
            print('model save: {}'.format(model))
    except IntegrityError as err:
        print(err)
    if hasattr(model, 'password'):
        try:
            model.set_password(model.password)
            model.save()
            return model
        except Exception as err:
            print(err)
            return None
class Command(BaseCommand):
    """Scraping Command"""
    help = 'initialize scrapers by setting up tracking database entries'

    def handle(self, *args, **options):
        """run command"""
        # =================================================================
        #
        #==================================================================
        all_models = []
        # =================================================================
        # load job skills
        #==================================================================

        for skill in SKILLS:
            for level in LEVELS:
                jobskill = JobSkill(name=skill, about=ABOUT, level=level)
                # all_models.append(jobskill)

        # =================================================================
        # load job seeker profiles
        #==================================================================
        names = chain(zip(MALE_NAMES, SURNAMES), zip(FEMALE_NAMES, SURNAMES))
        for first_name, surname in names:
            username = ''.join((first_name,surname)).lower()
            password = PASSWORD
            email = EMAIL_GENERATOR.generate()
            user = User(username=username, password=password, email=email,
                        first_name=first_name, last_name=surname)
            user = save_model(user)
            if user:
                dob = datetime.date(*random.choice(DATES))
                mobile = '0702006545'
                experience = random.choice(list(range(15)))
                industry = random.choice(INDUSTRIES)
                edu = random.choice(EDU)
                gender = random.choice(GENDERS)
                location = random.choice(LOCATIONS)


                seeker = JobSeekerProfile(user=user, about='about seeker', dob=dob,
                                          mobile=mobile, experience=experience,
                                          industry=industry, edu=edu, location=location)
                save_model(seeker)
                for _ in range(3):
                    skill = random.choice(JobSkill.objects.all())
                    if not skill in seeker.skills.all():
                        seeker.skills.add(skill)
                save_model(seeker)
        # ====================================================================
        # load recruiters
        # ====================================================================
        for first_name, surname in RECRUITERS:
            username = ''.join((first_name,surname)).lower()
            password = PASSWORD
            email = EMAIL_GENERATOR.generate()
            user = User(username=username, password=password, email=email,
                        first_name=first_name, last_name=surname)
            user = None # save_model(user)
            if user:
                about = 'about recruiter'
                company = random.choice(COMPANIES)

                recruiter = RecruiterProfile(user=user, about=about, company=company)
                save_model(recruiter)
        # ====================================================================
        # load job profiles
        # ====================================================================
        for recruiter in []: #RecruiterProfile.objects.all():
            title = generate_title()
            desc = 'About job'
            experience = random.choice(list(range(15)))
            industry = random.choice(INDUSTRIES)
            edu = random.choice(EDU)
            gender = random.choice(GENDERS)
            location = random.choice(LOCATIONS)
            owner = recruiter
            skill = random.choice(JobSkill.objects.all())
            min_age = random.choice(list(range(20,30)))
            max_age = random.choice(list(range(40,60)))

            job = JobProfile(title=title, desc=desc, gender=gender, owner=recruiter,
                             industry=industry, location=location, experience=experience,
                             min_age=min_age, max_age=max_age, edu=edu)
            save_model(job)
            job.skills.add(skill)
            save_model(job)
