# Create your views here.
from rest_framework.decorators import api_view, authentication_classes

from myapp import utils
from myapp.auth.authentication import AdminTokenAuthtication
from myapp.handler import APIResponse
from myapp.models import Classification, Thing, Tag, Company
from myapp.permission.permission import isDemoAdminUser
from myapp.serializers import ThingSerializer, UpdateThingSerializer, CompanySerializer


@api_view(['GET'])
def list_user_company_api(request):
    if request.method == 'GET':
        userId = request.GET.get('userId', None)
        if userId:
            companies = Company.objects.filter(user=userId)
            serializer = CompanySerializer(companies, many=True)
            return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['POST'])
def create(request):

    companies = Company.objects.filter(user=request.data['user'])
    if companies and len(companies) > 0:
        return APIResponse(code=1, msg='已创建过了')

    serializer = CompanySerializer(data=request.data)
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
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    serializer = CompanySerializer(company, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='查询成功', data=serializer.data)
    else:
        print(serializer.errors)
        utils.log_error(request, '参数错误')

    return APIResponse(code=1, msg='更新失败')


@api_view(['POST'])
def delete(request):

    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        Company.objects.filter(id__in=ids_arr).delete()
    except Company.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')
    return APIResponse(code=0, msg='删除成功')
