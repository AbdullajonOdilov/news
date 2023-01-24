from rest_framework.filters import OrderingFilter, SearchFilter
from .serializers import NewsSerializer
from .models import News
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .pagination import CustomPagination


class NewsViewSet(viewsets.ModelViewSet): #4 and 5
    queryset = News.objects.all().order_by('-date')
    serializer_class = NewsSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['name']
    ordering_fields = ['date']
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10


# I also performed CRUD via APIView
# class NewsAPIView(APIView):
#
#     permission_classes = [IsAuthenticated,]
#     def get(self, request):
#         news = News.objects.all().order_by('-date')
#         ser = NewsSerializer(news, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         ser = NewsSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         return Response(ser.errors)
# class NewAPIView(APIView):
#     permission_classes = [IsAuthenticated,]
#
#     def get(self,request,pk):
#         news = News.objects.filter(id=pk)
#         ser = NewsSerializer(news, many=True)
#         return Response(ser.data)
#
#     def put(self, request, pk):
#         new = News.objects.get(id=pk, user=request.user)
#         ser = NewsSerializer(new, data=request.data)
#         if ser.is_valid():
#             ser.save()
#             result = {'info': 'news was updated', 'added info': ser.data}
#             return Response(result)
#         return Response({'msg': 'Smth went wrong'})
#     def delete(self,request, pk):
#         new = News.objects.get(id=pk)
#         if new.user==request.user:
#             new.delete()
#             return Response({"Success": "deleted"})
#         return Response({'info': "smth went wrong"})




