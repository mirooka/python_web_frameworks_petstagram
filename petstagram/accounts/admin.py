from django.contrib import admin

# Register your models here.
from petstagram.accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # inlines = (PetInLineAdmin,)
    list_display = ('first_name', 'last_name')