from django.db import models
from django.contrib.auth.models import User
from PIL import Image



subject = (
    ('Computer Science','Computer Science'),
    ('Artificial Intelligence','Artificial Intelligence'),
    ('Web Development','Web Development'),
    ('Web Designing','Web Designing'),
    ('Internert Of Things','Internert Of Things'),
)
colleges = (
    ('Adi Sankara Institute Of Engineering And Technology','Adi Sankara Institute Of Engineering And Technology'),
    ('Federal Institute of Science And Technology','Federal Institute of Science And Technology'),
    ('Union Christian College','Union Christian College'),
    ('Indian Institute Of Technology','Indian Institute Of Technology'),
    ('Rajagiri College of Management & Applied Sciences','Rajagiri College of Management & Applied Sciences'),
)

class InstitutionProfile(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)

	image = models.ImageField(default='default.png',upload_to='institution_profile_pics')
	college = models.CharField(max_length=556,choices=colleges,default="Your college")


	def __str__(self):
		return f'{self.user.username} InstitutionProfile'

	def save(self,**kwargs):
		super().save()
		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)	

			


class TeacherProfile(models.Model):
	image = models.ImageField(default='default.png',upload_to='teacher_profile_pics')
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	expertise = models.CharField(max_length=224, choices=subject,default="Your expertise")
	college = models.CharField(max_length=556,choices=colleges,default="Your college")

	video = models.FileField(upload_to = 'teacher_video',null=True)

	def __str__(self):
		return f'{self.user.username} TeacherProfile'

	def save(self,**kwargs):
		super().save()
		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)


class StudentProfile(models.Model):
	image = models.ImageField(default='default.png',upload_to='student_profile_pics')
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	college = models.CharField(max_length=556,choices=colleges,default="Your college")
	number = models.CharField(max_length=14,default="91")
	home = models.TextField(default="your home address")
	
	def __str__(self):
		return f'{self.user.username} StudentProfile'

	def save(self,**kwargs):
		super().save()
		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)
