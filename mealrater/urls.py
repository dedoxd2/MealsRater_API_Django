from django.contrib import admin
from django.urls import path
# from django.conf.urls import include, path
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('gettoken/', obtain_auth_token),

]
