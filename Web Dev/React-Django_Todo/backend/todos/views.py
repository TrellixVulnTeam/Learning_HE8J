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

'''
uisng class views
'''
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