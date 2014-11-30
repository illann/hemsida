from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

    # The additional attributes we wish to include.
	foretag = models.CharField(max_length=50, blank=True)
	orgnr = models.CharField(max_length=50, blank=True)
	foretagsbeskrivning = models.TextField(blank=True)
	is_buyer = models.BooleanField(default=True)
	address = models.CharField(max_length=50, blank=True)
	stad = models.CharField(max_length=50, blank=True)
	postnr = models.CharField(max_length=50, blank=True)

	

	def __unicode__(self):
		return self.user.username
	
	
	User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])