from django.urls import path
from . import views


urlpatterns = [
    path('',views.card,name="card"),
    path('signup/', views.signup_view, name="signup"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.logout_view, name="logout"),
    path('create/', views.addtask, name='addtask'),
    path('updatetask/<int:task_id>/',views.updatetask,name='updatetask'),
    path('complete/<int:task_id>/',views.complete,name="complete"),
    path('compltetask/<int:task_id>/', views.completetask, name='completetask'),
    path('delete/<int:task_id>/',views.deletetask,name='deletetask'),
    # path('complete/',views.completetask,name="complete")


]