from django.contrib import admin

# Register your models here.
from app1.models import Lawyer,User

admin.site.register(User)
admin.site.register(Lawyer)