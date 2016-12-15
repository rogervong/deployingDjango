from __future__ import unicode_literals
from ..logandreg.models import User
from django.db import models
from datetime import datetime
# Create your models here.
class PlanManager(models.Manager):
	def validate(self, destination, description, start, end):
		errors= {}
		if len(destination) < 1:
			errors['destination'] = "Input a destination"
		if len(description) < 1:
			errors['description'] = "Input a description"
		try:
			datetime.strptime(start, "%Y-%m-%d")
			if datetime.strptime(start, "%Y-%m-%d") < datetime.now():
				errors['start'] = 'Invalid start time'
		except:
			errors['start'] = 'Invalid start time'
		try:
			datetime.strptime(end, "%Y-%m-%d")
			if datetime.strptime(end, "%Y-%m-%d") > datetime.now():
				pass
		except:
			errors['start'] = 'Invalid end time'
		if end < start:
			errors['end'] = 'End time cannot be before start time'
		if errors:
			return(False, errors)
		return(True, "")
class Plan(models.Model):
	destination = models.CharField(max_length = 100)
	description = models.TextField(max_length = 1000)
	user = models.ForeignKey(User, null=True)
	start = models.DateField()
	end = models.DateField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	planManager = PlanManager()

class Travel(models.Model):
	user = models.ForeignKey(User, null=True)
	plan = models.ForeignKey(Plan, null=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
