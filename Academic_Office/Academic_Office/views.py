from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Login_student
def home(request):
	return render(request,'Academic_Office/Home_page.html')
from Student.models import Students

def Student_login(request):
	form = Login_student()
	if request.method == 'POST':
		form=Login_student(request.POST)
		if form.is_valid():
			S_id=form.cleaned_data['S_id'].lower()
			if Students.objects.filter(S_id=S_id).count()==1:
				db=Students.objects.get(S_id=S_id)
				if form.cleaned_data['password']==db.S_password:
					request.session['S_id'] = S_id
					request.session['password'] = db.S_password
					s='/Students/'+S_id
					return HttpResponseRedirect(s)

				else:
					return render(request,'Academic_Office/No_password.html')
			else:
				return render(request,'Academic_Office/No_user.html')
		else:
			return render(request,'Academic_Office/login_student.html',{'form':form,'errs':form.errors})
	else:
		if('S_id' in request.session)&('password' in request.session):
			return render(request,'Academic_Office/logged_in.html',{"student":db})

		form=Login_student()
	return render(request,'Academic_Office/login_student.html',{'form':form})

def logout(request):
	del request.session['S_id']
	del request.session['password']
	return render(request,'Academic_Office/Home_page.html')
