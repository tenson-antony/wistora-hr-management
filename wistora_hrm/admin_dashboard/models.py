from django.db import models
from django.contrib.auth.models import User


# 1. Department Management
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.department_name


# 2. Employee Management
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True
    )
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()
    phone = models.CharField(max_length=15)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Active', 'Active'),
            ('Inactive', 'Inactive'),
        ],
        default='Active'
    )

    def __str__(self):
        return self.user.username


# 3. Student Management
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    placement_status = models.CharField(
        max_length=30,
        choices=[
            ('Registered', 'Registered'),
            ('Training', 'Training'),
            ('Placed', 'Placed'),
            ('Not Placed', 'Not Placed'),
        ],
        default='Registered'
    )

    def __str__(self):
        return self.user.username


# 4. Student Attendance / Placement Training
class TrainingSession(models.Model):
    session_title = models.CharField(max_length=150)
    training_type = models.CharField(
        max_length=50,
        choices=[
            ('Aptitude', 'Aptitude'),
            ('Technical', 'Technical'),
            ('Interview', 'Interview'),
            ('Soft Skills', 'Soft Skills'),
        ]
    )
    session_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    trainer_name = models.CharField(max_length=150)

    def __str__(self):
        return self.session_title


class StudentAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(
        TrainingSession, on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent'),
            ('Late', 'Late'),
        ]
    )
    marked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'session'],
                name='unique_student_training_attendance'
            )
        ]

    def __str__(self):
        return f"{self.student} - {self.session}"


# 5. Leave Management
class LeaveType(models.Model):
    leave_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.leave_name


class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(
        LeaveType, on_delete=models.PROTECT
    )
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Approved', 'Approved'),
            ('Rejected', 'Rejected'),
        ],
        default='Pending'
    )
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} - {self.status}"


# 6. Authentication and User Roles
class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_name = models.CharField(
        max_length=50,
        choices=[
            ('Admin', 'Admin'),
            ('HR', 'HR'),
            ('Employee', 'Employee'),
            ('Placement Officer', 'Placement Officer'),
            ('Student', 'Student'),
        ]
    )
    assigned_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.role_name}"


# 7. Client Management
class Client(models.Model):
    client_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Active', 'Active'),
            ('Inactive', 'Inactive'),
        ],
        default='Active'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name


# 8. Reports and Analytics
class ReportLog(models.Model):
    report_name = models.CharField(max_length=150)
    report_type = models.CharField(max_length=100)
    generated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.report_name


# 9. Notifications
class Notification(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField()
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# 10. Admin Activity Tracking
class AuditLog(models.Model):
    admin = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    action = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action

# Create your models here