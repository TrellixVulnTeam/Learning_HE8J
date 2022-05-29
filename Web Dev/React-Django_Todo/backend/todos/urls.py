from posixpath import basename
from venv import create
from django.db import router
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views

'''
Method one is the commented one, the api-view method
Method two is the bottom one, we use generics class view
'''
app_name = 'todos'
urlpatterns = [
    path('', views.api_root, name = "api-root"),
    # path('todos/', views.todoList, name="todo-list"),
    # path('todos/<int:pk>', views.todoDetails, name="todo-detail"),
    # path('todo-create/', views.todoCreate, name="todo-create"),
	# path('todo-update/<str:pk>/', views.todoUpdate, name="todo-update"),
	# path('todo-delete/<str:pk>/', views.todoDelete, name="todo-delete"),

    path('todos/', views.TodoList.as_view(), name = "todo-list"),
    path('todos/<int:pk>', views.TodoDetail.as_view(), name = "todo-detail")
 
]
urlpatterns = format_suffix_patterns(urlpatterns)


'''
Method three, we use viewsets
'''
todo_list = views.TodoViewSet.as_view( {
    'get': 'list',
    'post': 'create'
    })

todo_detail = views.TodoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
'''
urlpatterns = [
     path('todos/', todoList, name="todo-list"),
     path('todos/<int:pk>', todoDetails, name="todo-detail"),
]

or can just use router
and skip all above binding

router = DefaultRouter()
router.register(r'todos', views.TodoViewSet, basename="todos")
urlpatterns = [
    path('', include(router._urls))
]

'''