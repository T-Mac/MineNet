from django.db import models

class Client(models.Model):
	user = models.CharField(max_length=200)
	sessionid = models.CharField(max_length=200)
	md5 = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.md5
		
		
class Server(models.Model):
	name = models.CharField(max_length=200)
	uuid = models.CharField(max_length=200)
	ip_address = models.CharField(max_length=200)
	has_pass = models.BooleanField()
	password = models.CharField(max_length=200)
	
	def __unicode__(self):	
		return self.name
# Create your models here.
