from django.db import models
from django.contrib.auth.models import User
from article.models import Article

# Create your models here.


class Offert(models.Model):
	owner = models.ForeignKey(User)
	article_owner = models.ForeignKey(Article)
	body = models.TextField('Comment', blank=True)
	price = models.PositiveIntegerField('Price')
	
