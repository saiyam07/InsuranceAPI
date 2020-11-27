'''
URL paatterns to redirect to appropriate service handler
'''
from django.urls import path,include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('auth/',include('authservice.urls'))
]
