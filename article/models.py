from django.db import models
from django.contrib.auth.models import User
from userprofile.models import UserProfile
import datetime
from time import time
from random import randint



def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)
	

	
# Create your models here.
class Article(models.Model):
	owner = models.ForeignKey(User)
	
	title = models.CharField('Title', max_length=200)
	body = models.TextField()
	pub_date = models.DateField(("Publish date"), default=datetime.date.today)
	del_date = models.CharField('Delivery date', blank = True, max_length=20)
	q_date = models.DateField('Last date for offers')
	kategori = models.CharField('Category', max_length=100)
	filer = models.FileField(upload_to=get_upload_file_name, blank=True)
	state = models.BooleanField('Aktiv', default = True)
	quotation_amount = models.PositiveIntegerField('Antal inkomna offerter', default=0)
	
	#-------------------Prisintervall------------------------------------
	Lowprice = models.PositiveIntegerField(default = 0, blank = True)
	intervall = models.CharField(default = 0, blank = True, max_length=100)
	int1 = models.PositiveIntegerField(default = 0, blank = True)
	int2 = models.PositiveIntegerField(default = 0, blank = True)
	int3 = models.PositiveIntegerField(default = 0, blank = True)
	int4 = models.PositiveIntegerField(default = 0, blank = True)
	int5 = models.PositiveIntegerField(default = 0, blank = True)
	int6 = models.PositiveIntegerField(default = 0, blank = True)
	int7 = models.PositiveIntegerField(default = 0, blank = True)
	int8 = models.PositiveIntegerField(default = 0, blank = True)
	int9 = models.PositiveIntegerField(default = 0, blank = True)
	

	def __unicode__(self):
		return self.title
		
class Offert(models.Model):
	owner = models.ForeignKey(User)
	article_owner = models.ForeignKey(Article)
	body = models.TextField('Comment', blank=True)
	price = models.PositiveIntegerField('Price')
	title = models.CharField(default = 'Offert', max_length=200)
		
	def __unicode__(self):
		return self.title
	
