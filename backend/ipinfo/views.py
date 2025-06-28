from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import IPAddress
from .serializers import IPListSerializer,IPAddressSerializer
from .tasks import fetch_ip,process_ip_info

class IPSubmitView(APIView):
    def post(self, request):
        serializer = IPListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ips = serializer.validated_data["ips"]
        task_ids = []

        for ip in ips:
            result = fetch_ip.delay(ip)
            task_ids.append({ip: result.id})

        return Response({
            "message": "Tasks submitted",
            "task_ids": task_ids
        })
class IPSubmitprocessView(APIView):
    def post(self, request):
        serializer = IPListSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            for ip in data["ips"]:
                process_ip_info.delay(ip)
            return Response({'message': 'IP info fetch tasks initiated.', 'data': data}, status=202)
        return Response(serializer.errors, status=400)





class IPAddressListView(generics.ListAPIView):
    queryset = IPAddress.objects.all().order_by('-created_at')
    serializer_class = IPAddressSerializer 