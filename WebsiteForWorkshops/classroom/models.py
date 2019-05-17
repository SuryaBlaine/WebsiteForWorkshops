from django.db import models
from django.contrib.auth.models import User
from user.models import TeacherProfile,StudentProfile
from django.utils import timezone

class classroom(models.Model):
	host = models.ForeignKey(User,on_delete = models.CASCADE)
	teacher = models.ForeignKey(TeacherProfile,on_delete = models.CASCADE)
	title = models.CharField(max_length = 256)
	subtitle = models.CharField(max_length = 257,default='')
	venue = models.TextField(default='youre venue address')
	description = models.TextField()
	fee = models.CharField(max_length=15) 
	date_posted = models.DateTimeField(default=timezone.now)
	date_of_class = models.DateTimeField(default=timezone.now)
	additional_info = models.TextField(default='guidelines etc...')

	def save(self):
		return super().save()

	def __str__(self):
		return f'{self.title} by {self.host} @ {self.date_of_class}'

	def get_absolute_url(self):
		return reverse(kwargs={'pk':self.pk})


class classroomjoin(models.Model):
	classroom = models.ForeignKey(classroom,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	
	def __str__(self):
		return f'{self.classroom.title}'

class classroomteach(models.Model):
	classroom = models.ForeignKey(classroom,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	
	def __str__(self):
		return f'teaching {self.classroom.title}'