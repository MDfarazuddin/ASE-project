from django.shortcuts import render
from django.http import HttpResponse
from Teacher.models import Teachers
from Student.models import Students
# Create your views here.

def admin_home(request):
	return render(request,'Admin/Admin_View_home.html')

def admin_view_profile(request):
	return render(request,'Admin/Admin_View_View_Profiles.html')

def admin_add_teacher(request):
	return	render(request,'Admin/Admin_View_Add_Teacher.html')

def admin_add_student(request):
	return render(request,'Admin/Admin_View_Add_Student.html')


def teacher_list(request):
	all_teachers = Teachers.objects.all()
	return render(request,'Admin/teacher_list.html',{"all_teachers":all_teachers})
	# return HttpResponse("dfjkhfjk")


def student_list(request):
	all_students = Students.objects.all()
	return render(request,'Admin/student_list.html',{"all_students":all_students	})
	# return HttpResponse("dfjkhfjk")

