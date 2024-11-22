from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser 

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    # Extend UserAdmin to include the custom fields
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Register the custom user model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin) 