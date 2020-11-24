from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view()
def hello_world(request):
    return Response({"message": "Hello, World"})


@api_view(['GET', 'POST'])
def hello(request):
    if request.method == 'GET':
        return Response({"message": "hello world"})
    elif request.method == 'POST':
        return Response({'message': 'hello {}'.format(request.data['name'])})


@api_view(['GET', 'POST'])
def calculator(request):
    try:
        num1 = request.data['num1']
        num2 = request.data['num2']
        opr = request.data['opr']
    except:
        return Response({"error": "enter commands correctly"},
                        status=status.HTTP_400_BAD_REQUEST)

    else:
        if isinstance(num1, int) and isinstance(num2, int):

            if opr == '+':
                return Response({"result": num1 + num2}, status=status.HTTP_200_OK)
            elif opr == '-':
                return Response({"result": num1 - num2}, status=status.HTTP_200_OK)
            elif opr == '*':
                return Response({"result": num1 * num2}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "wrong operator"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Send integer values"},
                            status=status.HTTP_400_BAD_REQUEST)
