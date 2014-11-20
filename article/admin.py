from django.contrib import admin
from article.models import Article
# Import the UserProfile model individually.
#from article.models import UserProfile

# Register your models here.

admin.site.register(Article)
#admin.site.register(UserProfile)
