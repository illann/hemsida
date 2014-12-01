from django.contrib import admin
from article.models import Article, Offert
# Import the UserProfile model individually.
#from article.models import UserProfile

# Register your models here.

admin.site.register(Article)
admin.site.register(Offert)

#admin.site.register(UserProfile)
