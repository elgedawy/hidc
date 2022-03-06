
from apps.home.models import Request
from .models import Request
from .serializers import RequestSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def request_list_api(request):
    req_list = Request.objects.all()
    data = RequestSerializer(req_list, many=True).data
    return Response({'data': data})

@api_view(['GET'])
def request_detail_api(request, id):
    req_list = Request.objects.get(id=id)
    data = RequestSerializer(req_list).data
    return Response({'data': data})




class RequestDetail(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    lookup_field = 'id'


 