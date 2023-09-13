from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TEAM_CHOICE = (
    ('OAK'),
    ('PIT'),
    ('SD'),
    ('SEA'),
    ('SF'),
    ('STL'),
    ('TB'),
    ('TEX'),
    ('TOR'),
    ('MIN'),
    ('PHI'),
    ('ATL'),
    ('CWS'),
    ('MIA'),
    ('NYY'),
    ('MIL'),
    ('LAA'),
    ('AZ'),
    ('BAL'),
    ('BOS'),
    ('CHC'),
    ('CIN'),
    ('CLE'),
    ('COL'),
    ('DET'),
    ('HOU'),
    ('KC'),
    ('LAD'),
    ('WSH'),
    ('NYM'),
)

POSITION_CHOICE = (
    ('2B'),
    ('C'),
    ('SS'),
    ('P'),
    ('DH'),
    ('LF'),
    ('RF'),
    ('CF'),
    ('1B')
)

BATS_THROWS_CHOICE = (
    ('R'),
    ('L')
)

HITS_POWER_GIELDING_THROWING_RUN_CHOICE = (
    ('30'),
    ('40'),
    ('45'),
    ('50'),
    ('55'),
    ('60'),
    ('70'),
    ('80')
)



# class PlayerHitter(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=False)
#     lastName = models.CharField(max_length=200, null=True)
#     firstName = models.CharField(max_length=200, null=True)
#     team = models.CharField(max_length=3, choices=TEAM_CHOICE, default='OAK')
#     position = models.CharField(max_length=3, choices=POSITION_CHOICE, default='2B')
#     bats = models.CharField(max_length=1, choices=BATS_THROWS_CHOICE, default='R')
#     throws = models.CharField(max_length=1, choices=BATS_THROWS_CHOICE, default='L')
#     reportDate = models.DateTimeField(auto_now_add=True)
#     declarativeStatement = models.TextField(null=True)
#     hit = models.IntegerField(label="Hit", widget=models.ChoiceField(choices=HITS_POWER_GIELDING_THROWING_RUN_CHOICE))
#     hitFv = models.ChoiceField(null=True, choices=HITS_POWER_GIELDING_THROWING_RUN_CHOICE)
#     hitComment = models.TextField(null=True)
#     power = models.ChoiceField(null=True, choices=HITS_POWER_GIELDING_THROWING_RUN_CHOICE, default=30)
#     powerFv = models.ChoiceField(null=True, choices=HITS_POWER_GIELDING_THROWING_RUN_CHOICE, default=30)
#     powerComment = models.TextField(null=True)
#     fielding = models.ChoiceField(null=True, choices=HITS_POWER_GIELDING_THROWING_RUN_CHOICE, default=30)
#     fieldingFv = models.ChoiceField(null=True, choices=HITS_POWER_GIELDING_THROWING_RUN_CHOICE, default=30)
#     fieldingComment = models.TextField(null=True)
#     throwing = models.ChoiceField(null=True, choices=HITS_POWER_GIELDING_THROWING_RUN_CHOICE, default=30)
#     throwingFv = models.ChoiceField(null=True, choices=HITS_POWER_GIELDING_THROWING_RUN_CHOICE, default=30)
#     throwingComment = models.TextField(null=True)
#     run = models.ChoiceField(null=True, choices=HITS_POWER_GIELDING_THROWING_RUN_CHOICE, default=30)
#     runFv = models.ChoiceField(null=True, choices=HITS_POWER_GIELDING_THROWING_RUN_CHOICE, default=30)
#     runComment = models.TextField(null=True)
#     overallGrade = models.ChoiceField(null=True, choices=HITS_POWER_GIELDING_THROWING_RUN_CHOICE, default=30)
#     futureGrade = models.ChoiceField(null=True, choices=HITS_POWER_GIELDING_THROWING_RUN_CHOICE, default=30)
#     createdAt = models.DateTimeField(auto_now_add=True)
#     id = models.AutoField(primary_key=True, editable=False)


