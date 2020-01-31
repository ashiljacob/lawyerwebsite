from django.conf.urls import url
from django.contrib import admin

from app1 import views

urlpatterns = [
    url(r'^$', views.main_home, name="main_home"),
    url(r'^user/$', views.user,name="user"),
    url(r'^user_dash/$', views.user_dash, name="user_dash"),
    url(r'^reg/$',views.registration,name='reg'),
    url(r'^reg_upload/$',views.reg_upload,name='reg_upload'),
    url(r'^casefiling/$',views.casefiling,name='casefiling'),
    # url(r'^test/$',views.test),
    url(r'^admin/', admin.site.urls),
    url(r'^lawyer/$',views.law),
    url(r'^lawyerdash/$',views.lawyerdash,name="lawyerdash"),

]
