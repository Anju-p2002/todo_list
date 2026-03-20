from django.urls import path
from . import views


urlpatterns = [
    path('example/',views.example,name="example"),
    path('',views.card,name="card"),
    # path('login/', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.logout_view, name="logout"),
    path('create/', views.addtask, name='addtask'),


]