from django.conf.urls import url
from dapp import views

app_name='dapp'


urlpatterns=[


    url('users',views.users,name='users'),
    url('user_login',views.user_login,name='user_login'),
    url('gallery', views.gal,name='gal')


]