from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',include('home.urls')),
    path('home/',include('home.urls')),
    path('accounts/',include('user.urls')),
    path('classroom/',include('classroom.urls'))

]


if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)