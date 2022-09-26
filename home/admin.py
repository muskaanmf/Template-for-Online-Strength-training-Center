from django.contrib import admin 
from home.models import Contacts, Exercise
from home.models import Subscribe
# Register your models here.

admin.site.register(Contacts)
admin.site.register(Subscribe)
admin.site.register(Exercise)

