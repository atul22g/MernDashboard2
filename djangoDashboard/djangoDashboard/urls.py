from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authApp.urls')),
    path('dashboard/', include('dashboard.urls'))
]

urlpatterns += staticfiles_urlpatterns()