from django.contrib import admin
#from dapp.models import employee
from dapp.models import userprofileinfo
# Register your models here.

"""class Employeeadmin(admin.ModelAdmin):
    list_display = ['id','eno','enmae','esal']
admin.site.register(employee,Employeeadmin)"""
admin.site.register(userprofileinfo)
