
# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models 
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

 #Displaying these fields in the admin(in this order).
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')

    #These fields become in links to the profile main page.
    list_display_links = ('pk', 'user')

    #You can edit these field's content without going to the profile main page.
    list_editable = ('phone_number', 'website', 'picture')

    #You can search in the browser bar by these days.
    search_fields = (
        'user__email', 
        'user__username',
        'user__first_name', 
        'user__last_name', 
        'phone_number',
    )

    #You can filter by these fields(in this order).
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created', 
        'modified',
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )      
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)