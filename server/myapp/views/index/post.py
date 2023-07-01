# Create your views here.
from rest_framework.decorators import api_view, authentication_classes

from myapp import utils
from myapp.auth.authentication import AdminTokenAuthtication
from myapp.handler import APIResponse
from myapp.models import Post
from myapp.permission.permission import isDemoAdminUser
from myapp.serializers import PostSerializer


@api_view(['GET'])
def list_user_post_api(request):
    if request.method == 'GET':
        userId = request.GET.get("userId", None)
        if userId is None:
            return APIResponse(code=1, msg='userId不能为空')

        posts = Post.objects.filter(user=userId).order_by('-create_time')
        serializer = PostSerializer(posts, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def list_company_post_api(request):
    if request.method == 'GET':
        companyId = request.GET.get("companyId", None)
        if companyId is None:
            return APIResponse(code=1, msg='companyId不能为空')

        posts = Post.objects.filter(company=companyId).order_by('-create_time')
        serializer = PostSerializer(posts, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)

@api_view(['POST'])
def create(request):

    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)
    else:
        print(serializer.errors)
        utils.log_error(request, '参数错误')

    return APIResponse(code=1, msg='创建失败')
