from django.contrib import admin

from mySite.models import *
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(User)
