from django.contrib import admin
from .models import Tbl_teacher,Tbl_student_teacher,Tbl_student,Tbl_student_class,Tbl_class,Tbl_assignment
# Register your models here.

#Tbl_class_admin
class Tbl_class_admin(admin.ModelAdmin):
    list_display = ('class_id', 'class_name', 'class_info','class_module','assignment_id','teacher_id')
admin.site.register(Tbl_class,Tbl_class_admin)

#Tbl_assignment_admin
class Tbl_assignment_admin(admin.ModelAdmin):
    list_display = ('assignment_id', 'assignment_name', 'assignment_percentage','assignment_due','class_id')
admin.site.register(Tbl_assignment,Tbl_assignment_admin)

#Tbl_teacher_admin
class Tbl_teacher_admin(admin.ModelAdmin):
    list_display = ('teacher_id', 'teacher_name', 'teacher_email')
admin.site.register(Tbl_teacher,Tbl_teacher_admin)

#Tbl_student_teacher_admin
class Tbl_student_teacher_admin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'teacher_id')
admin.site.register(Tbl_student_teacher,Tbl_student_teacher_admin)

#Tbl_student_admin
class Tbl_student_admin(admin.ModelAdmin):
    list_display = ( 'student_id', 'student_name','student_email')
admin.site.register(Tbl_student,Tbl_student_admin)

#Tbl_student_class_admin
class Tbl_student_class_admin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'class_id')
admin.site.register(Tbl_student_class,Tbl_student_class_admin)