from django.contrib import admin
from Users.models import Users

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['email', 'firstname', 'lastname', 'othernames', 'username', 'isadmin', 'phone', 'referral_code','location', 'profilepic']
    # list_filter = ('typeOfBus',)
