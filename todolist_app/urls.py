from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import TodoListView, TodoCreate, TodoUpdateView, TodoDeleteView, TodoAssigned, TodoDetailView

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view()),
    path('login/', auth_views.LoginView.as_view()),
    path('', TodoListView.as_view(), name='todo_list'),
    path('create/', TodoCreate.as_view(), name='todo_create'),
    path('edit/<pk>', TodoUpdateView.as_view(), name='todo_update'),
    path('assigned/<pk>', TodoAssigned.as_view(), name='todo_assigned'),
    path('delete/<pk>', TodoDeleteView.as_view(), name='todo_delete'),
    path('view/<pk>', TodoDetailView.as_view(), name='todo_view'),
]
