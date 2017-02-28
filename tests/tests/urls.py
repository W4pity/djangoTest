"""tests URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include #include do not forget to include
#files
from django.contrib import admin
#from blog import views
#from . import views #to include relative views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.index, name='index'), # relative and rename it for the url
    #url(r'^blog/', views.home), #not forget to add blog in installed app in
    #setting file
    #url(r'^blog/', include ('blog.urls')), We can also create a file urls in blog
    url(r'^', include('blog.urls')),#it's the no url i think
]
