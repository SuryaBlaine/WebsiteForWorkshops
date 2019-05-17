from django.shortcuts import render,redirect
from . forms import (
	UserRegisterForm,
	createstudentprofileform,
	createteacherprofileform,
	createinstitutionprofileform,
	studentprofileeditform,
	teacherprofileeditform,
	institutionprofileeditform,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView
from . models import StudentProfile,TeacherProfile,InstitutionProfile
from django.urls import reverse_lazy

def home(request):
	return render(request,'user/home.html')


class studentprofileedit(UpdateView):
	model = StudentProfile
	fields = ['image','college','number','home']
	template_name = "user/profileedit.html"
	success_url = reverse_lazy('profile')

	def form_valid(self,form):
		quiz = form.save(commit=False)
		quiz.user = self.request.user
		quiz.save()
		return redirect('profile')


class teacherprofileedit(UpdateView):
	model = TeacherProfile
	fields = ['image','college','expertise','video']
	template_name = "user/profileedit.html"
	success_url = reverse_lazy('profile')

	def form_valid(self,form):
		quiz = form.save(commit=False)
		quiz.user = self.request.user
		quiz.save()
		return redirect('profile')


class institutionprofileedit(UpdateView):
	model = InstitutionProfile
	fields = ['image','college']
	template_name = "user/profileedit.html"
	success_url = reverse_lazy('profile')

	def form_valid(self,form):
		quiz = form.save(commit=False)
		quiz.user = self.request.user
		quiz.save()
		return redirect('profile')




def register(request):

	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			
			return redirect('signin')
	else:
		form = UserRegisterForm()

	return render(request,'user/register.html',{'form':form})


@login_required
def profile(request):
	context = {
		'student':StudentProfile,
		'teacher':TeacherProfile,
		'institution':InstitutionProfile
	}
	return render(request,'user/profile.html',context)



@login_required
def createstudentprofile(request):
	if request.method == 'POST':
		form = createstudentprofileform(request.POST,request.FILES)
		form.instance.user = request.user
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = createstudentprofileform()

	return render(request,'user/profilecreate.html',{'form':form})

@login_required
def createteacherprofile(request):
	if request.method == 'POST':
		form = createteacherprofileform(request.POST,request.FILES)
		form.instance.user = request.user
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = createteacherprofileform()

	return render(request,'user/profilecreate.html',{'form':form})

@login_required
def createinstitutionprofile(request):
	if request.method == 'POST':
		form = createinstitutionprofileform(request.POST,request.FILES)
		form.instance.user = request.user
		if form.is_valid():
			form.save()
			
			
			return redirect('home')
	else:
		form = createinstitutionprofileform()

	return render(request,'user/profilecreate.html',{'form':form})

