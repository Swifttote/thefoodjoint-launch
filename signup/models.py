from django.db import models

from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class TrialClass(models.Model):
	nameType = models.TextField(max_length = 10)

	def __unicode__(self):
		return unicode(self.id)


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	contactinfo = PhoneNumberField()

	def __unicode__(self):
		return unicode(self.user.username) 

