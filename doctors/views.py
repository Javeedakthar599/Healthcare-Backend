from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Doctor
from .serializers import DoctorSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def doctors(request):

    if request.method == 'GET':

        doctors = Doctor.objects.filter(created_by=request.user)

        serializer = DoctorSerializer(doctors, many=True)

        return Response(serializer.data)


    if request.method == 'POST':

        serializer = DoctorSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(created_by=request.user)

            return Response(serializer.data)

        return Response(serializer.errors)
