from django.contrib import admin
from django.contrib import admin
from ContactEnquiry.models import contactEnquiry # type: ignore
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','referral','date','occassion','location','currency','budget','comments')
    
admin.site.register(contactEnquiry,ContactAdmin) 

# Register your models here.
