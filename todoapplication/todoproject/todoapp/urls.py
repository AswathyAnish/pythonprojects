from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('details', views.details, name='details'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('classview/', views.Tasklistview.as_view(), name='classview'),
    path('classdetailview/<int:pk>/', views.Taskdetailview.as_view(), name='classdetailview'),
    path('classupdateview/<int:pk>/', views.Taskupdateview.as_view(), name='classupdateview'),
    path('classdeleteview/<int:pk>/', views.Taskdeleteview.as_view(), name='classdeleteview'),

]
