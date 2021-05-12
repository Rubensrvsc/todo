from django.urls import path,include
from .views import *

urlpatterns = [
    path('',TaskViewCreate.as_view(),name="task-create"),
    path('list-task',TaskViewList.as_view(),name="task-list"),
    path('create-user',UserViewCreate.as_view(),name="create-user")
]