from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from .models import Todo
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import TodoSerializer, UserCreationSerializer, UserSerializer

User = get_user_model()

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

@api_view(['POST'])
# 로그인을 하지 않아도 요청 허용
@permission_classes((AllowAny, ))
def user_signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save()의 return 값은 User 모델의 인스턴스
        user = serializer.save()
        # User model의 인스턴스가 갖고 있는 set_password -> 인자는 raw password가 들어감
        user.set_password(request.data.get('password'))
        user.save()
        print(serializer.data)
        return Response({'message': '회원가입이 성공적으로 완료되었습니다.'})

@api_view(['GET'])
def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    if request.user != user:
        # Response(status=403) 과 동일
        return HttpResponseForbidden()
    serializer = UserSerializer(user)
    return Response(serializer.data)