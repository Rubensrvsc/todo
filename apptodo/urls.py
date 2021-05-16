from django.urls import path,include
from .views import *
from rest_framework.authtoken import views

urlpatterns = [
    path('',TaskViewCreate.as_view(),name="task-create"),
    path('list-task',TaskViewList.as_view(),name="task-list"),
    path('create-user',UserViewCreate.as_view(),name="create-user"),
    path('task/<int:id>',TaskRetrieve.as_view(),name='retrieve'),
    path('obtain-token',views.obtain_auth_token,name="obtain-token"),
    path('obter',ObterTokenView.as_view(),name='obter')
]