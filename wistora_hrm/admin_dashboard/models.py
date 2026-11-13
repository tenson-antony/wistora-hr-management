from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.TextField(blank=True)
    def __str__(self):
        return self.name

class Designation(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='designations')
    title=models.CharField(max_length=100)

    class Meta:
        unique_together=('department','title')

        def __str__(self):
            return f"{self.department.name} - {self.title}"
class Employee(models.Model):
    STATUS_CHOICES=[
        ('Active','Active'),
        ('Inactive','Inactive'),
        ('On Leave','On Leave'),
    ]
    employee_id=models.CharField(max_length=20,unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    department=models.ForeignKey(Department,on_delete=models.PROTECT,related_name='employees')
    designation=models.ForeignKey(Designation,on_delete=models.PROTECT,related_name='employees')
    joining_date=models.DateField()  
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='Active')   

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_id})"   

class EmployeeProfile(models.Model):
    employee=models.OneToOneField(Employee,on_delete=models.CASCADE,related_name='profile')
    phone=models.CharField(max_length=15,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    address=models.TextField(blank=True)
    profile_photo=models.ImageField(upload_to='employee_photos/',null=True,blank=True)

    def __str__(self):
        return f"{self.employee.first_name}'s profile"