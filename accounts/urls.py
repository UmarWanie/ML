from django.urls import path
from .import views

app_name = "accounts"

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/',  views.signin, name = 'signin'),
    path('signout/', views.signout, name= 'signout'),
    path('ad_login/', views.ad_login, name= 'ad_login'),
    path('predict/', views.predict, name = 'predict'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('myTable/', views.myTable, name = 'myTable'),
    path('predict_opd/', views.predict_opd, name = 'predict_opd'),
    path('profile/', views.profile, name = 'profile')

]