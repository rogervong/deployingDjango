from __future__ import unicode_literals

from django.db import models
import bcrypt

class UserManager(models.Manager):
	def login(self, username, password):
		try:
			user = self.get(username=username)
			if bcrypt.hashpw(password.encode('utf-8'), user.password.encode('utf-8')) == user.password:
				return(True, user)
		except:
			# raise
			print 'hello'
			return(False,{"login": "login failed"})
		return(False,{"login": "login failed"})

	def register(self, name, username, password, confirm_password,):
		errors={}
		if len(name) < 3:
			errors['name'] = "Name is too short"
		if len(username) < 3:
			errors['username'] = "Username is too short"
		if len(password) < 8:
			errors['password'] = "Password is too short"
		if password != confirm_password:
			errors['confirm_password'] = "Passwords must match"
			pass
		if errors:
			return(False, errors)
		password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
		self.create(name=name, username=username, password=password,)
		return(True, self.get(username=username))
# Create your models here.
class User(models.Model):
	name = models.CharField(max_length = 45)
	username = models.CharField(max_length = 45)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()
