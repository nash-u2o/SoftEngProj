from django.db import models


# Default auto=incrementing primary key
# Make username unique
# Make email unique
# Have a password
# Use username and password to login
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=320)
    name = models.CharField(max_length=50)
    student = models.BooleanField(default=True)


class Test(models.Model):
    creator_id = models.IntegerField(primary_key=True)
    text = models.TextField()


# Tbl_class
"""
* class_info should be a TextField
* module should be a separate class
* I don't see how foreign key for assignment_id does much
"""


class Tbl_class(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=200)
    class_info = models.TextField()
    class_module = models.TextField()
    teacher_id = models.IntegerField()


# Tbl_assignment


class Tbl_assignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    assignment_name = models.CharField(max_length=200)
    assignment_percentage = models.CharField(max_length=200)
    assignment_due = models.CharField(max_length=200)
    class_id = models.IntegerField()


# Tbl_teacher
class Tbl_teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=200)
    teacher_email = models.EmailField(max_length=200, unique=True)
    teacher_password = models.CharField(max_length=200, default="pass")


# Tbl_student_teacher
class Tbl_student_teacher(models.Model):  # Don't know if this table is necessary
    student_id = models.IntegerField()
    teacher_id = models.IntegerField()


# when storing password, use make_password from django.contrib.auth.hashers import make_password
# Tbl_student
class Tbl_student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=200)
    student_email = models.EmailField(max_length=200, unique=True)
    student_password = models.CharField(max_length=200, default="pass")


# Tbl_student_class
class Tbl_student_class(models.Model):
    student_id = models.IntegerField()
    class_id = models.IntegerField()
