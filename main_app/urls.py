from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', TaskViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('tasks/', task_list, name='task_list'),
    path('', home, name='home'),
    path("register/", register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout')
]

