from django.conf.urls import url
from seguridad import views

# SET THE NAMESPACE!
app_name = 'seguridad'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='login'),
]