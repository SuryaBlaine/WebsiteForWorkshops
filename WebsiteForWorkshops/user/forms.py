from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentProfile,TeacherProfile,InstitutionProfile
from PIL import Image

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','password1','password2']
###################################################
class createstudentprofileform(forms.ModelForm):
	class Meta:
		model = StudentProfile
		fields = ['image','college','number','home']
	 

class createteacherprofileform(forms.ModelForm):
	class Meta:
		model = TeacherProfile
		fields = ['image','college','expertise','video']  

class createinstitutionprofileform(forms.ModelForm):
	class Meta:
		model = InstitutionProfile
		fields = ['image','college'] 

###################################################
class studentprofileeditform(forms.ModelForm):
	class Meta:
		model = StudentProfile
		fields = ['image','college','number','home']
	 

class teacherprofileeditform(forms.ModelForm):
	class Meta:
		model = TeacherProfile
		fields = ['image','college','expertise','video']  

class institutionprofileeditform(forms.ModelForm):
	class Meta:
		model = InstitutionProfile
		fields = ['image','college'] 