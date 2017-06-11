
from django.conf.urls import include, url
from django.contrib import admin
from rapipd import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^all/', include('rapipd.urls')),
    url(r'^newdata', views.newData)
]
