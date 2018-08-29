"""myWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.conf.urls import url
from myWebsiteApp.views import  homepage,about_us,our_products,contact_us,newCars
from  django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$',homepage),
    url('^about_us/$',about_us),
    url('^our_products/$', our_products),
    url('^contact_us/$', contact_us),
    url('^newCars/$', newCars),



]

urlpatterns += staticfiles_urlpatterns()

