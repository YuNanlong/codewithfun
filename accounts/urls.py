from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', views.my_login, name='login'),
    url(r'^logout/$', views.my_logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^edit/password/$', views.change_pwd, name='edit_pwd'),
    url(r'^edit/learned_course/$', views.learned_course, name='learned_course'),
    url(r'^password/change/$', auth_views.password_change, name='password_change'),
    url(r'^password/change/done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^resetpassword/$', auth_views.password_reset, {'template_name': 'password_reset.html'}, name='password_reset'),
    url(r'^resetpassword/passwordsent/$', auth_views.password_reset_done, {'template_name': 'password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
]
