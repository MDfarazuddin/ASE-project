from django.shortcuts import render

from django.http import HttpResponse

from . models import Teachers

def Teacher_Profile(request,slug):
	a_teacher = Teachers.objects.get(slug=slug)	
	return render(request,'Teacher/Teacher_View.html',{"a_teacher":a_teacher})