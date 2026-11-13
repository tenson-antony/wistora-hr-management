from django.db import models

# Create your models here.

from django.db import models


class Student(models.Model):

    # Student status
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('graduated', 'Graduated'),
        ('discontinued', 'Discontinued'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    # 1. Personal Information
    student_id = models.CharField(max_length=20, unique=True)
    register_number = models.CharField(max_length=30, unique=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True
    )

    date_of_birth = models.DateField(null=True, blank=True)

    # 2. Contact Information
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    # 3. Academic Information
    department = models.CharField(max_length=100)
    course = models.CharField(max_length=150)

    batch = models.CharField(
        max_length=20,
        help_text="Example: 2026-2029"
    )

    academic_year = models.CharField(
        max_length=20,
        blank=True,
        help_text="Example: 2026-2027"
    )
    semester = models.PositiveSmallIntegerField(
    null=True,
    blank=True
    )

    semester = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )

    admission_date = models.DateField(null=True, blank=True)

    # 4. Parent / Guardian Information
    guardian_name = models.CharField(max_length=150, blank=True)
    guardian_relationship = models.CharField(max_length=50, blank=True)
    guardian_phone = models.CharField(max_length=15, blank=True)
    guardian_email = models.EmailField(blank=True)

    # 5. Student Status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    # 6. Record Tracking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = "Student"
        verbose_name_plural = "Students"
