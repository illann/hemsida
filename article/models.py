from django.db import models
from django.contrib.auth.models import User
from userprofile.models import UserProfile
import datetime


"""
def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

"""

# Create your models here.
class Article(models.Model):
	owner = models.ForeignKey(User)
	
	title = models.CharField('Titel', max_length=200)
	body = models.TextField('Beskrivning')
	pub_date = models.DateTimeField(default=datetime.date.today)
	del_date = models.DateTimeField('Leveransdatum')
	kvalitetskrav = models.CharField('Kvalitetskrav', max_length=100)
	material = models.CharField('Material', max_length=100)
	#kategori = models.CharField('Material', max_length=100)

	#likes = models.IntegerField(default=0)
	#thumbnail = models.FileField(upload_to=get_upload_file_name)
	

		
	def __unicode__(self):
		return self.title
		
class Offert(models.Model):
	owner = models.ForeignKey(User)
	article_owner = models.ForeignKey(Article)
	body = models.TextField('Comment', blank=True)
	price = models.PositiveIntegerField('Price')
	

		
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

    # The additional attributes we wish to include.
	foretag = models.CharField(max_length=30, blank=True)
	avdelning = models.CharField(max_length=30, blank=True)

    # Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username

"""
