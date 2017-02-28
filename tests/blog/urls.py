from django.conf.urls import url, include #include do not forget to include
#files
#from blog import views
from . import views #to include relative views

urlpatterns = [
    url(r'^', views.index, name='index'), # relative and rename it for the url
]
