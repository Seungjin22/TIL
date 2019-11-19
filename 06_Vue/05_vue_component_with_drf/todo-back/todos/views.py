from django.shortcuts import render, get_object_or_404
from .models import Todo
from rest_framework.response import Response
from .serializers import TodoSerializer
from rest_framework.decorators import api_view, permission_classes

@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save() # Todo 라는 모델의 인스턴스가 나옴
        # serializer.data -> Json ({ 'id': 1, 'user': 1, 'title': 첫 번째 할 일, 'completed': false })
        return Response(serializer.data)
    return Response(status=400)


@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'PUT':
        # 기존 todo에서 request.POST(수정 내용)으로 변경
        serializer = TodoSerializer(todo, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            # save하고 Json으로 응답
            return Response(serializer.data)
        # 유효하지 않으면 에러 메세지와 함께 400 에러
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        todo.delete()
        # 204 -> 해당하는 컨텐츠가 없는 경우(todo를 삭제했기 때문에 해당하는 todo가 존재하지 않음을 알려줌)
        return Response(status=204)