from django.urls import path
from .views import TodoListView, TodoDetailView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Homepage
    path('api/todos/', TodoListView.as_view(), name='todo-list'),  # API endpoint for todos
    path('api/todos/<str:todo_id>/', TodoDetailView.as_view(), name='todo-detail'),  # API endpoint for specific todo
]