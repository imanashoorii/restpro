from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def hello_world(request):
    return Response({"message": "Hello, World"})


@api_view(['GET', 'POST'])
def hello(request):
    if request.method == 'GET':
        return Response({"message": "Hello, World"})
    elif request.method == 'POST':
        return Response({'message': 'Hello, {}'.format(request.data['name'])})
