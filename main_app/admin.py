import email

from django.contrib import admin

from main_app.models import Student

# Register your models here.
# customize the header
admin.site.site_header = 'ST Francis Boys'


class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'kcpe_score', 'email'
                    ]
    # the search functionality

    search_fields = ['first_name'', "kcpe_score', 'is_spoty']
    list_filter = ["is_spoty"]
    list_per_page = 50



admin.site.register(Student, StudentAdmin)
