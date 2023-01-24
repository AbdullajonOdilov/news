from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import News
from .serializers import NewsSerializer

class NewsAPIView(APIView):
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    ordering_fields = ['name']

    def get(self, request):
        news = News.objects.all().order_by('-date')
        ser = NewsSerializer(news, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = NewsSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors)
class NewAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def put(self, request, pk):
        new = News.objects.get(id=pk, user=request.user)
        ser = NewsSerializer(new, data=request.data)
        if ser.is_valid():
            ser.save()
            result = {'info': 'news was updated', 'added info': ser.data}
            return Response(result)
        return Response({'msg': 'Smth went wrong'})
    def delete(self,request, pk):
        new = News.objects.get(id=pk)
        if new.user==request.user:
            new.delete()
            return Response({"Success": "deleted"})
        return Response({'info': "smth went wrong"})



