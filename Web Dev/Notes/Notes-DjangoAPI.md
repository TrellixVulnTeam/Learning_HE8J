# Django

- [Django](#django)
  - [api_view Decorators](#api_view-decorators)
  - [API view](#api-view)
  - [API View Generics](#api-view-generics)
  - [Viewset](#viewset)
- [URLS](#urls)

mainly used for backend frameworks
Models, Views (functions), Template (Looks)

refer to React-Django-Project

Either use APIView or Use GenericView or ModelViewSets
(Lots of built in)

---

## api_view Decorators

```python
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.reverse import reverse
# Create your views here.
'''
using decorators
'''
@api_view(['GET'])
def api_root(request):
    api_urls = {
        'todos': reverse('todos:todo-list'),
    }
    return Response(api_urls)

@api_view(['GET'])
def todoList(request):
	todos = Todo.objects.all().order_by('-id')
	serializer = TodoSerializer(todos, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def todoDetails(request, pk):
	data = Todo.objects.get(id=pk)
	serializer = TodoSerializer(data, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def todoCreate(request):
	serializer = TodoSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def todoUpdate(request, pk):
    date = Todo.objects.get(id=pk)
    serializer = TodoSerializer(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def todoDelete(request, pk):
	todo = Todo.objects.get(id=pk)
	todo.delete()

	return Response('Item succsesfully delete!')
```

## API view

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
```

---

## API View Generics

```python
class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    '''
    you can create your custom get,put,post,delete mehthods here
    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    '''
```

---

## Viewset

```python
class TodoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    #custom methods that dont fit in standard list bla bal bla, URLs are by default same as method name
    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     snippet = self.get_object()
    #     return Response(snippet.highlighted)
```

# URLS

```py
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
```
