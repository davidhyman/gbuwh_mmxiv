from django.db import models
from django.contrib.auth.models import User

class Membership(models.Model):
    """
    Extensions to the User model
    """
    address = models.CharField(max_length=256)
    telephone = models.CharField(max_length=30)
    
    # these fields are intended for club captains etc, but could be used by anyone
    public_address = models.CharField(max_length=256)
    public_telephone = models.CharField(max_length=30)
    
    # the officially registered membership is to this club
    club = models.ForeignKey(Club)
    
    #sessions = models.ManyToManyField(Session) # track/display 'my sessions' etc

class MemberRoles(models.Model):
    """
    Named roles for members. Nothing to do with website permissions (yet - may be needed for website/squad management).
    """
    name = models.CharField(max_length=30)
    # different groups of roles for different circumstances
    is_club = models.BooleanField() # club roles, e.g. pres/sec/treas/web etc
    is_gbuwh = models.BooleanField() # gbuwh roles e.g. chair/sec/treas/web/elite captain etc
    
class Club(models.Model):
    """
    A club entity as governed by GBUWH
    """
    name = models.CharField(max_length=64)

class Session(models.Model):
    """
    A club can run several sessions
    """
    address = models.CharField(max_length=256)
    # some kind of geolocation fields for mapping, possibly extracted from the address
    location = None
    # some kind of recurrence/date management
    # maybe https://github.com/django-recurrence/django-recurrence
    # alternatively use google calendars
    calendar_info = None