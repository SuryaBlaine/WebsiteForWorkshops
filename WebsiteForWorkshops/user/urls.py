from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('', views.register,name='registerhome'),

	path('profile/', views.profile,name='profile'),
	path('profile/edit/<int:pk>/s/', views.studentprofileedit.as_view(),name='studentprofileedit'),
	path('profile/edit/<int:pk>/t/', views.teacherprofileedit.as_view(),name='teacherprofileedit'),
	path('profile/edit/<int:pk>/i/', views.institutionprofileedit.as_view(),name='institutionprofileedit'),
	path('profile/student/create/', views.createstudentprofile,name='createstudentprofile'),
	path('profile/teacher/create/', views.createteacherprofile,name='createteacherprofile'),
	path('profile/institution/create/', views.createinstitutionprofile,name='createinstitutionprofile'),



    path('register/', views.register,name='register'),
    path('signin/',auth_views.LoginView.as_view(template_name='user/signin.html'),name='signin'),
    path('signout/',auth_views.LogoutView.as_view(template_name='user/signout.html'),name='signout'),
]
