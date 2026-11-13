from django.db import models

# Create your models here.


# Class Management
class Class(models.Model):
    class_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.class_name


# Subject Management
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20, unique=True)

    class_name = models.ForeignKey(
        Class,
        on_delete=models.PROTECT,
        related_name="subjects"
    )

    description = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name


# Academic Session Management
class AcademicSession(models.Model):
    session_name = models.CharField(max_length=50, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.session_name
