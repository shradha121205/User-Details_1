from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class UserAdmin(admin.ModelAdmin):
    # Fields that should be searchable in the admin panel
    search_fields = ['employee_id', 'first_name','last_name']

    # Optionally, you can define other customizations, like list display
    list_display = ('employee_id', 'first_name','last_name','email','phone_number','hire_date','job_title','department','salary','manager_id','date_of_birth'
                    )

