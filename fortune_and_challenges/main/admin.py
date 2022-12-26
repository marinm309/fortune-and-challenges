from django.contrib import admin
from . models import Fortune, UserFortune, Challenge

admin.site.register(Fortune)
admin.site.register(UserFortune)
admin.site.register(Challenge)
