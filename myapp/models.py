from django.db import models

class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    hire_date = models.DateField()
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    salary = models.FloatField()
    manager_id = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'employee'  # or 'shrad_employee', if you prefer the same naming convention
