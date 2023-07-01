# Create your views here.
from rest_framework.decorators import api_view, authentication_classes

from myapp import utils
from myapp.auth.authentication import AdminTokenAuthtication
from myapp.handler import APIResponse
from myapp.models import Resume
from myapp.permission.permission import isDemoAdminUser
from myapp.serializers import ResumeSerializer



@api_view(['GET'])
def detail(request):

    try:
        user = request.GET.get('user', -1)
        resumes = Resume.objects.filter(user=user)
        print(resumes)
    except Resume.DoesNotExist:
        utils.log_error(request, '对象不存在')
        return APIResponse(code=1, msg='对象不存在')

    if request.method == 'GET':
        if resumes and len(resumes) > 0:
            serializer = ResumeSerializer(resumes[0])
            return APIResponse(code=0, msg='查询成功', data=serializer.data)
        else:
            return APIResponse(code=1, msg='不存在')



@api_view(['POST'])
def create(request):

    resumes = Resume.objects.filter(user=request.data['user'])
    if resumes and len(resumes) > 0:
        return APIResponse(code=1, msg='已创建过了')

    serializer = ResumeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)
    else:
        print(serializer.errors)
        utils.log_error(request, '参数错误')

    return APIResponse(code=1, msg='创建失败')


@api_view(['POST'])
def update(request):


    try:
        pk = request.GET.get('id', -1)
        resume = Resume.objects.get(pk=pk)
    except Resume.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    serializer = ResumeSerializer(resume, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='查询成功', data=serializer.data)
    else:
        print(serializer.errors)
        utils.log_error(request, '参数错误')

    return APIResponse(code=1, msg='更新失败')


