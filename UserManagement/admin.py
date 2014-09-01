from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group
from UserManagement.models import Member

admin.site.register(Member)
admin.site.unregister(Group)
