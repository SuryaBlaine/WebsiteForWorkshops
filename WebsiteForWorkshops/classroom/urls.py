from django.urls import path
from . import views
from . models import classroom
urlpatterns = [
	path('', views.classroomhome,name='classroomhome'),
	path('create/', views.ClassroomCreateView.as_view(),name='createclassroomview'),
	#path('<int:pk>/teach/', views.teachclassroomview,name='teachclassroomview'),
	path('<int:pk>/edit/', views.ClassroomEditView.as_view(),name='editclassroomview'),
	path('<int:pk>/join/', views.ClassroomJoinView.as_view(),name='joinclassroomview'),
	path('<int:pk>/view/', views.ClassroomDetailView.as_view(),name='detailclassroomview'),
	path('<int:pk>/delete/', views.ClassroomDeleteView.as_view(),name='deleteclassroomview'),
]
